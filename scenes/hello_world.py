from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#050505"

class HelloWorld(Scene):
    def construct(self):
        title = Text("MICHAŚ KURWA OSTRZEGA", font_size=48, color=WHITE)
        subtitle = Text("Manim render test", font_size=30, color=TEAL_A)
        subtitle.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle), run_time=0.7)
        self.wait(1)
