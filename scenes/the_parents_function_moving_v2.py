from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"


class TheParentsFunctionMovingV2(MovingCameraScene):
    def construct(self):
        # Kolory
        child_color = "#D946EF"    # neon magenta/fiolet
        parent_color = "#22D3EE"  # neon cyan
        grid_color = "#111111"    # bardzo subtelny grid

        # Nieskończona przestrzeń: duży NumberPlane
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

        # ValueTracker czasu / pozycji w przestrzeni
        t = ValueTracker(0)

        # Funkcje trajektorii (delikatne, żywe krzywe)
        def child_y(x):
            return -0.15 * x + 0.4 * np.sin(0.7 * x)

        def parent_y(x):
            return -0.12 * x + 0.3 * np.sin(0.7 * x + 0.5)

        # Zakres widocznej części trajektorii (od t-5 do t)
        def make_child_line():
            xs = np.linspace(t.get_value() - 5, t.get_value(), 200)
            ys = child_y(xs)
            points = np.column_stack([xs, ys, np.zeros_like(xs)])
            line = VMobject(color=child_color, stroke_width=6)
            line.set_points_smoothly(points)
            glow = line.copy().set_stroke(child_color, width=22, opacity=0.12)
            return VGroup(glow, line)

        def make_parent_line():
            xs = np.linspace(t.get_value() - 5, t.get_value(), 200)
            ys = parent_y(xs)
            points = np.column_stack([xs, ys, np.zeros_like(xs)])
            line = VMobject(color=parent_color, stroke_width=6)
            line.set_points_smoothly(points)
            glow = line.copy().set_stroke(parent_color, width=22, opacity=0.12)
            return VGroup(glow, line)

        child_line = always_redraw(make_child_line)
        parent_line = always_redraw(make_parent_line)
        self.add(child_line, parent_line)

        # Etykiety podążające za czo
