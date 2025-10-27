import viser
import plotly.graph_objects as go
import time
import math


server = viser.ViserServer()

# Set up example GPS data
gps_location = {"lon": -71.0565, "lat": 42.3555}
gps_fig = go.Figure()
gps_handle = server.gui.add_plotly(figure=gps_fig, aspect=1.0)

location_timer = 0.0
while True:
    # Simulate GPS location updates
    gps_fig.data = []
    gps_location["lon"] += math.sin(location_timer) * 0.00001
    gps_location["lat"] += math.cos(location_timer) * 0.00001

    # Add GPS location trace
    gps_fig.add_trace(
        go.Scattermap(
            mode="markers+lines",
            lon=[gps_location["lon"]],
            lat=[gps_location["lat"]],
            fill="toself",
            hoverinfo="text",
            hovertext="Location",
            marker=dict(
                size=10,
                color="red",
            ),
            line=dict(color="red"),
        )
    )

    # Center the map on the GPS location
    gps_fig.update_layout(
        map={
            "style": "open-street-map",
            "center": gps_location,
            "zoom": 15,
        },
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
    )

    # Update the figure and timer
    gps_handle.figure = gps_fig
    location_timer += 0.01
    time.sleep(0.01)
