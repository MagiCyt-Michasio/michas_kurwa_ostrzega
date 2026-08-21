        # Kropki
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

        # Napisy
        title = Text("TRZY PERSPEKTYWY", font_size=32, color=text_col)
        title.to_edge(UP, buff=0.5)
        self.add(title)
