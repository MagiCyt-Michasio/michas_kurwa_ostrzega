from manim import *

# Konfiguracja pionowa 9:16, 1080x1920, 60 FPS, czarne t
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 60
config.background_color = "#000000"


class TheParentsFunction(Scene):
    def construct(self):
        # Kolory
        child_color = "#D946EF"   # neon magenta/fiolet
        parent_color = "#22D3EE" # neon cyan/b
        world_color = "#C9D1D9"  # ch
        grid_color = "#111111"   # bardzo subtelny grid
        text_color = "#FFFFFF"

        # Siatka
        plane = NumberPlane(
            x_range=[-4.5, 4.5, 1],
            y_range=[-7, 7, 1],
            x_length=8.4,
            y_length=13.2,
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

        # Etykiety
        child_label = Text("The Child", font_size=28, color=child_color)
        parent_label = Text("The Parent", font_size=28, color=parent_color)
        world_label = Text("The World", font_size=28, color=world_color)

        child_label.move_to(plane.c2p(-3.4, -2.2))
        parent_label.move_to(plane.c2p(-3.4, -1.0))
        world_label.move_to(plane.c2p(0.0, 6.2))

        # Punkty startowe dla Parent i Child (lewa strona, blisko siebie)
        parent_start = [
            plane.c2p(-4.2, -0.8),
            plane.c2p(-2.8, -0.5),
            plane.c2p(-1.4, -0.3),
            plane.c2p(0.0, -0.15),
        ]
        child_start = [
            plane.c2p(-4.2, -2.0),
            plane.c2p(-2.8, -1.7),
            plane.c2p(-1.4, -1.5),
            plane.c2p(0.0, -1.35),
        ]

        parent_before = VMobject(color=parent_color, stroke_width=6)
        parent_before.set_points_smoothly(parent_start)
        child_before = VMobject(color=child_color, stroke_width=6)
        child_before.set_points_smoothly(child_start)

        # Glow
        parent_glow = parent_before.copy().set_stroke(parent_color, width=22, opacity=0.12)
        child_glow = child_before.copy().set_stroke(child_color, width=22, opacity=0.12)

        # Punkty
        parent_dot = Dot(parent_start[-1], radius=0.09, color=parent_color)
        child_dot = Dot(child_start[-1], radius=0.09, color=child_color)

        # The World: pionowa linia na środku
        world_line = Line(
            plane.c2p(0.0, 5.6),
            plane.c2p(0.0, -6.2),
            color=world_color,
            stroke_width=3,
        )
        world_glow = world_line.copy().set_stroke(world_color, width=18, opacity=0.09)

        # Impact point (miejsce, gdzie linie spotykają się z The World)
        impact_point = parent_start[-1]

        # Parent po załamaniu: gwałtowny spadek w dół
        parent_after_points = [
            plane.c2p(0.0, -0.15),
            plane.c2p(0.9, -4.8),
            plane.c2p(1.8, -3.9),
            plane.c2p(2.8, -3.1),
            plane.c2p(4.2, -2.6),
        ]
        parent_after = VMobject(color=parent_color, stroke_width=6)
        parent_after.set_points_smoothly(parent_start + parent_after_points[1:])
        parent_glow_after = parent_after.copy().set_stroke(parent_color, width=22, opacity=0.12)

        # Child po odbiciu: dynamiczny wzrost w górę
        child_after_points = [
            plane.c2p(0.0, -1.35),
            plane.c2p(0.9, 0.4),
            plane.c2p(1.8, 1.9),
            plane.c2p(2.8, 3.1),
            plane.c2p(4.2, 4.2),
        ]
        child_after = VMobject(color=child_color, stroke_width=6)
        child_after.set_points_smoothly(child_start + child_after_points[1:])
        child_glow_after = child_after.copy().set_stroke(child_color, width=22, opacity=0.12)

        # Tytuł końcowy (bezpieczny obszar, nie za nisko)
        title = Text("The Parent\'s Function", font_size=38, color=text_color)
        title.to_edge(DOWN, buff=1.1)

        # Sekwencja animacji
        self.add(plane)
        self.play(
            FadeIn(parent_label, shift=RIGHT * 0.12),
            FadeIn(child_label, shift=RIGHT * 0.12),
            run_time=0.6,
        )

        self.play(
            Create(parent_glow),
            Create(child_glow),
            Create(parent_before),
            Create(child_before),
            FadeIn(parent_dot, scale=0.5),
            FadeIn(child_dot, scale=0.5),
            run_time=2.2,
        )

        # Delikatny życiowy ruch obu linii przed uderzeniem
        self.play(
            parent_before.animate.shift(UP * 0.05),
            parent_glow.animate.shift(UP * 0.05),
            parent_dot.animate.shift(UP * 0.05),
            child_before.animate.shift(DOWN * 0.04),
            child_glow.animate.shift(DOWN * 0.04),
            child_dot.animate.shift(DOWN * 0.04),
            run_time=0.8,
            rate_func=there_and_back,
        )

        # Pojawienie się The World
        self.play(
            FadeIn(world_label, shift=DOWN * 0.12),
            Create(world_glow),
            Create(world_line),
            run_time=0.7,
            rate_func=rush_from,
        )

        # Uderzenie: Parent załamuje się w dół, Child odbija w górę
        self.play(
            Transform(parent_before, parent_after),
            Transform(parent_glow, parent_glow_after),
            Transform(child_before, child_after),
            Transform(child_glow, child_glow_after),
            parent_dot.animate.move_to(parent_after_points[-1]),
            child_dot.animate.move_to(child_after_points[-1]),
            FadeOut(world_line),
            FadeOut(world_glow),
            FadeOut(world_label),
            run_time=2.4,
            rate_func=smooth,
        )

        # Krótkie “oddychanie” Child po odbiciu
        self.play(
            child_before.animate.shift(UP * 0.06),
            child_glow.animate.shift(UP * 0.06),
            child_dot.animate.shift(UP * 0.06),
            run_time=0.7,
            rate_func=there_and_back,
        )

        # Tytuł końcowy
        self.play(FadeIn(title, shift=UP * 0.18), run_time=0.9)
        self.wait(1.4)
