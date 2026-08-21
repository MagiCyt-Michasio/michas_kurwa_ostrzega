from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"

class TrzyPerspektywy(MovingCameraScene):
    def construct(self):
        # Kolory
        grazynka_color = "#EB4BE1"
        fred_color = "#28EBF5"
        michas_color = "#78B4FF"
        grid_color = "#121212"
        text_color = "#F5F5F5"
        gold_color = "#00BEFF"

        # Duża przestrzeń
        plane = NumberPlane(
            x_range=[-100, 100, 1],
            y_range=[-100, 100, 1],
            x_length=80,
            y_length=80,
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

        # Trajektorie: Grazynka, Fred, Michas
        def traj_grazynka(x, t_val):
            phase = -0.25
            base = -0.055 * x + 0.25 * np.sin(0.55 * x + phase)
            offset = 0.65
            if t_val < 4.4:
                return base + offset
            elif t_val < 8.2:
                p = np.clip((t_val - 4.4) / (8.2 - 4.4), 0, 1)
                divergence = 1.05
                return base + (1 - p) * offset + p * divergence
            elif t_val < 10.2:
                p = np.clip((t_val - 8.2) / (10.2 - 8.2), 0, 1)
                common = -0.018 * x + 0.18 * np.sin(0.43 * x)
                return (1 - p) * (base + 1.05) + p * common
            else:
                return -0.018 * x + 0.18 * np.sin(0.43 * x)

        def traj_fred(x, t_val):
            phase = 0.0
            base = -0.055 * x + 0.25 * np.sin(0.55 * x + phase)
            offset = 0.0
            if t_val < 4.4:
                return base + offset
            elif t_val < 8.2:
                p = np.clip((t_val - 4.4) / (8.2 - 4.4), 0, 1)
                divergence = -0.95
                return base + (1 - p) * offset + p * divergence
            elif t_val < 10.2:
                p = np.clip((t_val - 8.2) / (10.2 - 8.2), 0, 1)
                common = -0.018 * x + 0.18 * np.sin(0.43 * x)
                return (1 - p) * (base - 0.95) + p * common
            else:
                return -0.018 * x + 0.18 * np.sin(0.43 * x)

        def traj_michas(x, t_val):
            phase = 0.25
            base = -0.055 * x + 0.25 * np.sin(0.55 * x + phase)
            offset = -0.65
            if t_val < 4.4:
                return base + offset
            elif t_val < 8.2:
                p = np.clip((t_val - 4.4) / (8.2 - 4.4), 0, 1)
                divergence = 0.35
                return base + (1 - p) * offset + p * divergence
            elif t_val < 10.2:
                p = np.clip((t_val - 8.2) / (10.2 - 8.2), 0, 1)
                common = -0.018 * x + 0.18 * np.sin(0.43 * x)
                return (1 - p) * (base + 0.35) + p * common
            else:
                return -0.018 * x + 0.18 * np.sin(0.43 * x)

        def make_line(traj_func, color):
            xs = np.linspace(t.get_value() - 5.7, t.get_value() + 0.55, 220)
            ys = traj_func(xs, t.get_value())
            pts = np.column_stack([xs, ys, np.zeros_like(xs)])
            line = VMobject(color=color, stroke_width=4)
            line.set_points_smoothly(pts)
            glow = line.copy().set_stroke(color, width=18, opacity=0.35)
            return VGroup(glow, line)

        grazynka_line = always_redraw(lambda: make_line(traj_grazynka, grazynka_color))
        fred_line = always_redraw(lambda: make_line(traj_fred, fred_color))
        michas_line = always_redraw(lambda: make_line(traj_michas, michas_color))
        self.add(grazynka_line, fred_line, michas_line)

        # Kropki na czo
