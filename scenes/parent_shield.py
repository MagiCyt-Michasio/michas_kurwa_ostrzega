from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#050505"


class ParentShield(Scene):
    def construct(self):
        parent_color = "#FF4F9A"
        child_color = "#56E8FF"
        world_color = "#FF4B4B"
        muted = "#9DA4B0"
        grid_color = "#121720"

        plane = NumberPlane(
            x_range=[-4.5, 4.5, 1],
            y_range=[-7, 7, 1],
            x_length=8.4,
            y_length=13.2,
            background_line_style={
                "stroke_color": grid_color,
                "stroke_width": 1,
                "stroke_opacity": 0.52,
            },
            faded_line_style={"stroke_opacity": 0},
            axis_config={
                "stroke_color": "#2A303A",
                "stroke_width": 2,
                "include_ticks": False,
            },
        )

        title = Text("FUNKCJA RODZICA", font_size=31, color=muted)
        title.to_edge(UP, buff=0.46)

        world_label = Text("ŚWIAT", font_size=27, color=world_color)
        world_label.move_to(plane.c2p(0, 6.05))

        parent_label = Text("RODZIC", font_size=25, color=parent_color)
        parent_label.move_to(plane.c2p(-3.35, -1.0))

        child_label = Text("DZIECKO", font_size=25, color=child_color)
        child_label.move_to(plane.c2p(-3.15, -2.15))

        parent_points_before = [
            plane.c2p(-4.15, -1.35),
            plane.c2p(-2.6, -0.8),
            plane.c2p(-1.0, -0.42),
            plane.c2p(0.0, -0.15),
        ]
        child_points_before = [
            plane.c2p(-4.15, -2.5),
            plane.c2p(-2.6, -1.9),
            plane.c2p(-1.0, -1.55),
            plane.c2p(0.0, -1.25),
        ]

        parent_points_after = [
            plane.c2p(0.0, -0.15),
            plane.c2p(0.72, -5.25),
            plane.c2p(1.45, -4.3),
            plane.c2p(2.35, -3.35),
            plane.c2p(4.15, -2.9),
        ]
        child_points_after = [
            plane.c2p(0.0, -1.25),
            plane.c2p(0.7, -1.03),
            plane.c2p(1.45, -0.84),
            plane.c2p(2.35, -0.5),
            plane.c2p(4.15, 0.28),
        ]

        parent_before = VMobject(color=parent_color, stroke_width=7)
        parent_before.set_points_smoothly(parent_points_before)
        child_before = VMobject(color=child_color, stroke_width=7)
        child_before.set_points_smoothly(child_points_before)

        parent_after = VMobject(color=parent_color, stroke_width=7)
        parent_after.set_points_smoothly(parent_points_before + parent_points_after[1:])
        child_after = VMobject(color=child_color, stroke_width=7)
        child_after.set_points_smoothly(child_points_before + child_points_after[1:])

        parent_glow = parent_before.copy().set_stroke(parent_color, width=25, opacity=0.14)
        child_glow = child_before.copy().set_stroke(child_color, width=25, opacity=0.14)
        parent_glow_after = parent_after.copy().set_stroke(parent_color, width=25, opacity=0.14)
        child_glow_after = child_after.copy().set_stroke(child_color, width=25, opacity=0.14)

        parent_dot = Dot(parent_points_before[-1], radius=0.09, color=parent_color)
        child_dot = Dot(child_points_before[-1], radius=0.09, color=child_color)

        impact_target = parent_points_before[-1]
        world_strike = Line(
            plane.c2p(0, 5.45),
            impact_target,
            color=world_color,
            stroke_width=8,
        )
        world_glow = world_strike.copy().set_stroke(world_color, width=30, opacity=0.13)

        impact = Dot(impact_target, radius=0.13, color=WHITE)
        impact_halo = Dot(impact_target, radius=0.46, color=world_color, fill_opacity=0.14, stroke_width=0)

        punchline = Text(
            "Nie usuwają bólu ze świata.\nStają między nim a dzieckiem.",
            font_size=35,
            color=WHITE,
            line_spacing=0.92,
        )
        punchline.to_edge(DOWN, buff=0.7)

        self.add(plane)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.65)
        self.play(
            FadeIn(parent_label, shift=RIGHT * 0.12),
            FadeIn(child_label, shift=RIGHT * 0.12),
            run_time=0.5,
        )

        self.play(
            Create(parent_glow),
            Create(child_glow),
            Create(parent_before),
            Create(child_before),
            FadeIn(parent_dot, scale=0.5),
            FadeIn(child_dot, scale=0.5),
            run_time=2.1,
        )

        self.play(
            parent_before.animate.shift(UP * 0.055),
            parent_glow.animate.shift(UP * 0.055),
            parent_dot.animate.shift(UP * 0.055),
            child_before.animate.shift(DOWN * 0.035),
            child_glow.animate.shift(DOWN * 0.035),
            child_dot.animate.shift(DOWN * 0.035),
            run_time=0.75,
            rate_func=there_and_back,
        )

        self.play(FadeIn(world_label, shift=DOWN * 0.12), run_time=0.45)
        self.play(Create(world_glow), Create(world_strike), run_time=0.55, rate_func=rush_from)

        self.play(
            FadeIn(impact_halo, scale=0.3),
            FadeIn(impact, scale=0.3),
            Flash(
                impact_target,
                color=world_color,
                flash_radius=1.0,
                line_length=0.32,
                num_lines=20,
                run_time=0.55,
            ),
            run_time=0.55,
        )

        self.play(
            Transform(parent_before, parent_after),
            Transform(parent_glow, parent_glow_after),
            Transform(child_before, child_after),
            Transform(child_glow, child_glow_after),
            parent_dot.animate.move_to(parent_points_after[-1]),
            child_dot.animate.move_to(child_points_after[-1]),
            FadeOut(world_strike),
            FadeOut(world_glow),
            FadeOut(world_label),
            FadeOut(impact),
            FadeOut(impact_halo),
            run_time=2.25,
            rate_func=smooth,
        )

        self.play(
            child_before.animate.shift(UP * 0.05),
            child_glow.animate.shift(UP * 0.05),
            child_dot.animate.shift(UP * 0.05),
            run_time=0.7,
            rate_func=there_and_back,
        )
        self.play(FadeIn(punchline, shift=UP * 0.18), run_time=0.9)
        self.wait(1.4)
