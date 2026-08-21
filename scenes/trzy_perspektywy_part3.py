        # Reveal
        self.camera.frame.remove_updater(update_camera)
        self.play(
            self.camera.frame.animate.move_to([9, 0, 0]),
            self.camera.frame.animate.set_width(100),
            run_time=2.5,
            rate_func=rate_functions.ease_in_out_cubic,
        )

        # Napisy
        g_label = Text("Grażynka", font_size=28, color=g_col)
        f_label = Text("Fred", font_size=28, color=f_col)
        m_label = Text("Michaś", font_size=28, color=m_col)

        g_label.next_to(g_dot, UP, buff=0.3)
        f_label.next_to(f_dot, UP, buff=0.3)
        m_label.next_to(m_dot, UP, buff=0.3)

        self.play(
            FadeIn(g_label, shift=UP*0.3),
            FadeIn(f_label, shift=UP*0.3),
            FadeIn(m_label, shift=UP*0.3),
            run_time=1.2,
        )

        # Koniec
        self.wait(1.5)
