        # Fazy
        phase1 = Text("1. Zaprzeczanie", font_size=28, color=text_col)
        phase1.move_to(axes.c2p(1.5, 4.5))
        self.add(phase1)

        phase2 = Text("2. Atak", font_size=28, color=red, weight=BOLD)
        phase2.move_to(axes.c2p(4.5, 4.5))
        self.add(phase2)

        phase3 = Text("3. Odwró···cenie r\u00f3l", font_size=28, color=dark_red)
        phase3.move_to(axes.c2p(7.5, 4.5))
        self.add(phase3)

        # Strzalki z napisami
        arrow1 = Arrow(
            axes.c2p(2.5, 2),
            axes.c2p(3.2, 3),
            color=arrow_col,
            stroke_width=8,
            buff=0,
        )
        note1 = Text("Uwaga – tu", font_size=20, color=arrow_col)
        note1.next_to(arrow1, UL, buff=0.2)
        self.add(arrow1, note1)

        arrow2 = Arrow(
            axes.c2p(5.5, 3.5),
            axes.c2p(6.2, 4.2),
            color=arrow_col,
            stroke_width=8,
            buff=0,
        )
        note2 = Text("co\u015b si\u0119", font_size=20, color=arrow_col)
        note2.next_to(arrow2, UL, buff=0.2)
        self.add(arrow2, note2)

        arrow3 = Arrow(
            axes.c2p(8, 2.5),
            axes.c2p(8.7, 3.2),
            color=arrow_col,
            stroke_width=8,
            buff=0,
        )
        note3 = Text("zaczyna dzia\u0107...", font_size=20, color=arrow_col)
        note3.next_to(arrow3, UL, buff=0.2)
        self.add(arrow3, note3)
