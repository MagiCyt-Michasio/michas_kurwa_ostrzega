from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"

class TheParentsFunctionMovingV5(MovingCameraScene):
    def construct(self):
        child_color = "#D946EF"
        parent_color = "#22D3EE"
        grid_color = "#111111"

        plane = NumberPlane(
            x_range=[-50, 50, 1],
            y_range=[-50, 50, 1],
            x_length=40,
            y_length=40,
            background_line_style={
                "stroke_color": grid_color,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
            faded_line_style={"stroke_opacity": 0},
            axis_config={
                "stroke_color": "#222222",
                "stroke_width": 2,
                "include_ticks": False,
            },
        )
        self.add(plane)

        t = ValueTracker(0)

        def child_y(x):
            return -0.15 * x + 0.4 * np.sin(0.7 * x)

        def parent_y(x):
            return -0.12 * x + 0.3 * np.sin(0.7 * x + 0.5)

        # Dwie kropki na czo
