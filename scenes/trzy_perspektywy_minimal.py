from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"

class TrzyPerspektywyMinimal(MovingCameraScene):
    def construct(self):
        g_col = "#EB4BE1"
        f_col = "#28EBF5"
        m_col = "#78B4FF"
        grid_col = "#121212"

        plane = NumberPlane(
            x_range=[-100, 100, 1],
            y_range=[-100, 100, 1],
            x_length=80,
            y_length=80,
            background_line_style={
                "stroke_color": grid_col,
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

        def traj_g(x, tv):
            base = -0.055*x + 0.25*np.sin(0.55*x - 0.25)
            off = 0.65
            if tv < 4.4: return base + off
            elif tv < 8.2:
                p = np.clip((tv-4.4)/3.8, 0, 1)
                return base + (1-p)*off + p*1.05
            elif tv < 10.2:
                p = np.clip((tv-8.2)/2.0, 0, 1)
                com = -0.018*x + 0.18*np.sin(0.43*x)
                return (1-p)*(base+1.05) + p*com
            else: return -0.018*x + 0.18*np.sin(0.43*x)

        def traj_f(x, tv):
            base = -0.055*x + 0.25*np.sin(0.55*x)
            off = 0.0
            if tv < 4.4: return base + off
            elif tv < 8.2:
                p = np.clip((tv-4.4)/3.8, 0, 1)
                return base + (1-p)*off + p*(-0.95)
            elif tv < 10.2:
                p = np.clip((tv-8.2)/2.0, 0, 1)
                com = -0.018*x + 0.18*np.sin(0.43*x)
                return (1-p)*(base-0.95) + p*com
            else: return -0.018*x + 0.18*np.sin(0.43*x)

        def traj_m(x, tv):
            base = -0.055*x + 0.25*np.sin(0.55*x + 0.25)
            off = -0.65
            if tv < 4.4: return base + off
            elif tv < 8.2:
                p = np.clip((tv-4.4)/3.8, 0, 1)
                return base + (1-p)*off + p*0.35
            elif tv < 10.2:
                p = np.clip((tv-8.2)/2.0, 0, 1)
                com = -0.018*x + 0.18*np.sin(0.43*x)
                return (1-p)*(base+0.35) + p*com
            else: return -0.018*x + 0.18*np.sin(0.43*x)

        def make_line(traj, col):
            xs = np.linspace(t.get_value()-5.7, t.get_value()+0.55, 220)
            ys = traj(xs, t.get_value())
            pts = np.column_stack([xs, ys, np.zeros_like(xs)])
            line = VMobject(color=col, stroke_width=4)
            line.set_points_smoothly(pts)
            glow = line.copy().set_stroke(col, width=18, opacity=0.35)
            return VGroup(glow, line)

        g_line = always_redraw(lambda: make_line(traj_g, g_col))
        f_line = always_redraw(lambda: make_line(traj_f, f_col))
        m_line = always_redraw(lambda: make_line(traj_m, m_col))
        self.add(g_line, f_line, m_line)

        g_dot = Dot(color=g_col, radius=0.15)
        f_dot = Dot(color=f_col, radius=0.15)
        m_dot = Dot(color=m_col, radius=0.15)
        self.add(g_dot, f_dot, m_dot)

        def update_dots(mob):
            ct = t.get_value()
            g_dot.move_to([ct, traj_g(ct, ct), 0])
            f_dot.move_to([ct, traj_f(ct, ct), 0])
            m_dot.move_to([ct, traj_m(ct, ct), 0])

        g_dot.add_updater(update_dots)
        f_dot.add_updater(update_dots)
        m_dot.add_updater(update_dots)

        def update_camera(mob):
            ct = t.get_value()
            cy = (traj_g(ct, ct) + traj_f(ct, ct) + traj_m(ct, ct)) / 3
            mob.move_to([0.92*ct, cy, 0])

        self.camera.frame.add_updater(update_camera)

        # Faza 1: wsp
