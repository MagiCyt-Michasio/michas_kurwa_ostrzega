        # Faza 1: wsp
        self.play(t.animate.set_value(4.4), run_time=4.4, rate_func=linear)

        # Faza 2: rozjazd
        self.play(t.animate.set_value(8.2), run_time=3.8, rate_func=linear)

        # Faza 3: synchronizacja
        self.play(t.animate.set_value(10.2), run_time=2.0, rate_func=linear)

        # Faza 4: wsp
        self.play(t.animate.set_value(18), run_time=7.8, rate_func=linear)
