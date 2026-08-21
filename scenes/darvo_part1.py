from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#0a0a0a"

class DARVO(MovingCameraScene):
    def construct(self):
        # Kolory
        red = "#ff3333"
        dark_red = "#880000"
        grid_col = "#1a1a1a"
        text_col = "#f0f0f0"
        arrow_col = "#ff6666"

        # Tlo - siatka
        plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            x_length=80,
            y_length=80,
            background_line_style={
                "stroke_color": grid_col,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
            faded_line_style={"stroke_opacity": 0},
        )
        self.add(plane)

        # Tytul
        title = Text("D.A.R.V.O.", font_size=42, color=red, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Osie
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 5, 1],
            x_length=7,
            y_length=4,
            axis_config={"color": text_col, "include_ticks": False},
        ).shift(DOWN*1)
        self.add(axes)

        # Etykiety osi
        x_label = Text("Czas", font_size=24, color=text_col).next_to(axes.x_axis, RIGHT)
        y_label = Text("Napięcie", font_size=24, color=text_col).next_to(axes.y_axis, UP)
        self.add(x_label, y_label)

        # Krzywa napięcia - D.A.R.V.O.
        def tension_curve(x):
            if x < 3:
                return 1 + 0.3*x  # Zaprzeczanie - powolny wzrost
            elif x < 6:
                return 1.9 + 0.8*(x-3)  # Atak - szybki wzrost
            else:
                return 4.3 - 0.5*(x-6)  # Odwrocenie - spadek (ofiara przejmuje winę)

        curve = axes.plot(tension_curve, color=red, stroke_width=5)
        glow = curve.copy().set_stroke(red, width=15, opacity=0.4)
        self.add(glow, curve)
