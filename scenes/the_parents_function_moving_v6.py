from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"

class TheParentsFunctionMovingV6(MovingCameraScene):
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

        def make_child_line():
            xs = np.linspace(t.get_value() - 5, t.get_value(), 200)
            ys = child_y(xs)
            pts = np.column_stack([xs, ys, np.zeros_like(xs)])
            line = VMobject(color=child_color, stroke_width=6)
            line.set_points_smoothly(pts)
            glow = line.copy().set_stroke(child_color, width=22, opacity=0.12)
            return VGroup(glow, line)

        def make_parent_line():
            xs = np.linspace(t.get_value() - 5, t.get_value(), 200)
            ys = parent_y(xs)
            pts = np.column_stack([xs, ys, np.zeros_like(xs)])
            line = VMobject(color=parent_color, stroke_width=6)
            line.set_points_smoothly(pts)
            glow = line.copy().set_stroke(parent_color, width=22, opacity=0.12)
            return VGroup(glow, line)

        child_line = always_redraw(make_child_line)
        parent_line = always_redraw(make_parent_line)
        self.add(child_line, parent_line)

        child_dot = Dot(color=child_color, radius=0.12)
        parent_dot = Dot(color=parent_color, radius=0.12)
        self.add(child_dot, parent_dot)

        def update_dots(mob):
            ct = t.get_value()
            child_dot.move_to([ct, child_y(ct), 0])
            parent_dot.move_to([ct, parent_y(ct), 0])

        child_dot.add_updater(update_dots)
        parent_dot.add_updater(update_dots)

        def update_camera(mob):
            ct = t.get_value()
            cy = child_y(ct)
            py = parent_y(ct)
            y_center = (cy + py) / 2
            # Kamera tak, żeby kropki były ok. 2.0 jednostki na prawo od środka kadru
            mob.move_to([ct - 2.0, y_center, 0])

        self.camera.frame.add_updater(update_camera)

        # Faza 1: lot przez przestrzeń (10s)
        self.play(t.animate.set_value(10), run_time=10, rate_func=linear)

        # Faza 2: rozdzielenie - Child w górę, Parent w dółłł (2s)
        self.play(
            child_dot.animate.move_to([t.get_value(), child_y(t.get_value()) + 6, 0]),
            parent_dot.animate.move_to([t.get_value(), parent_y(t.get_value()) - 6, 0]),
            run_time=2,
            rate_func=smooth,
        )

        self.wait(1)
