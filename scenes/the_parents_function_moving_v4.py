from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"

class TheParentsFunctionMovingV4(MovingCameraScene):
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

        child_label = Text("The Child", font_size=28, color=child_color)
        parent_label = Text("The Parent", font_size=28, color=parent_color)

        def update_labels(mob):
            ct = t.get_value()
            cy = child_y(ct)
            py = parent_y(ct)
            child_label.move_to([ct - 0.8, cy - 0.9, 0])
            parent_label.move_to([ct - 0.8, py + 0.9, 0])

        child_label.add_updater(update_labels)
        parent_label.add_updater(update_labels)
        self.add(child_label, parent_label)

        def update_camera(mob):
            ct = t.get_value()
            cy = child_y(ct)
            py = parent_y(ct)
            y_center = (cy + py) / 2
            # Chcemy, żeby czoло (x = ct) byто w ok. 65% szerokości kadru od lewej.
            # Środek kadru to mob.get_center()[0].
            # Lewa krawеdź = center_x - frame_width/2.
            # Chcemy: ct = left + 0.65 * frame_width
            # => center_x - frame_width/2 + 0.65*frame_width = ct
            # => center_x = ct + frame_width/2 - 0.65*frame_width
            frame_w = self.camera.frame_width
            center_x = ct + frame_w/2 - 0.65 * frame_w
            mob.move_to([center_x, y_center, 0])

        self.camera.frame.add_updater(update_camera)

        self.play(t.animate.set_value(12), run_time=10, rate_func=linear)
        self.wait(1)
