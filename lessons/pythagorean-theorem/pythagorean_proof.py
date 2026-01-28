from manim import *


def make_equation(parts, font_size=48):
    """Create equation from parts without LaTeX.
    parts: list of (text, color) tuples
    """
    group = VGroup()
    for text, color in parts:
        if "²" in text or text.isdigit() or text in "+=":
            t = Text(text, font_size=font_size, color=color)
        else:
            t = Text(text, font_size=font_size, color=color)
        group.add(t)
    group.arrange(RIGHT, buff=0.08)
    return group


class PythagoreanProof(Scene):
    def construct(self):
        # Triangle dimensions
        a = 1.2
        b = 1.6

        # Colors
        TRI_COLOR = BLUE
        TRI_FILL = BLUE_E
        A_COLOR = RED
        B_COLOR = GREEN
        C_COLOR = YELLOW

        # ═══════════════════════════════════════════════════════
        # PART 1: INTRODUCTION
        # ═══════════════════════════════════════════════════════

        title = Text("The Pythagorean Theorem", font_size=52)
        self.play(Write(title), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title))
        self.wait(0.5)

        # Show a right triangle
        intro_tri = Polygon(
            ORIGIN, RIGHT * 2, RIGHT * 2 + UP * 1.5,
            color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.6, stroke_width=3
        ).move_to(ORIGIN)

        self.play(Create(intro_tri), run_time=1.2)
        self.wait(1)

        # Label the sides one at a time
        tri_verts = intro_tri.get_vertices()

        label_a = Text("a", font_size=48, color=A_COLOR).next_to(intro_tri, DOWN, buff=0.2)
        explain_a = Text("(one leg)", font_size=24, color=GRAY).next_to(label_a, DOWN, buff=0.1)

        self.play(Write(label_a))
        self.play(FadeIn(explain_a))
        self.wait(1)

        label_b = Text("b", font_size=48, color=B_COLOR).next_to(intro_tri, RIGHT, buff=0.2)
        explain_b = Text("(other leg)", font_size=24, color=GRAY).next_to(label_b, RIGHT, buff=0.1)

        self.play(Write(label_b))
        self.play(FadeIn(explain_b))
        self.wait(1)

        # Hypotenuse with right angle marker
        ra_size = 0.2
        right_angle = VMobject(color=WHITE, stroke_width=2)
        right_angle.set_points_as_corners([
            tri_verts[1] + LEFT * ra_size,
            tri_verts[1] + LEFT * ra_size + UP * ra_size,
            tri_verts[1] + UP * ra_size
        ])
        self.play(Create(right_angle))
        self.wait(0.5)

        hyp_center = (tri_verts[0] + tri_verts[2]) / 2
        label_c = Text("c", font_size=48, color=C_COLOR).move_to(hyp_center + UL * 0.4)
        explain_c = Text("(hypotenuse)", font_size=24, color=GRAY)
        explain_c.next_to(label_c, UP, buff=0.15)

        self.play(Write(label_c))
        self.play(FadeIn(explain_c))
        self.wait(2)

        # Fade explanations
        self.play(FadeOut(explain_a), FadeOut(explain_b), FadeOut(explain_c))
        self.wait(0.5)

        # Show the theorem
        theorem_intro = Text("The theorem says:", font_size=32).to_edge(UP)
        self.play(Write(theorem_intro))
        self.wait(0.5)

        # Build equation: c² = a² + b²
        eq = make_equation([
            ("c²", C_COLOR), ("=", WHITE), ("a²", A_COLOR), ("+", WHITE), ("b²", B_COLOR)
        ], font_size=60)
        eq.move_to(UP * 2.3)

        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)

        # Transition
        self.play(
            FadeOut(intro_tri), FadeOut(label_a), FadeOut(label_b),
            FadeOut(label_c), FadeOut(right_angle), FadeOut(theorem_intro),
            FadeOut(eq)
        )
        self.wait(0.5)

        # ═══════════════════════════════════════════════════════
        # PART 2: WHY IS IT TRUE?
        # ═══════════════════════════════════════════════════════

        why_title = Text("But WHY is this true?", font_size=48)
        self.play(Write(why_title), run_time=1.2)
        self.wait(1.5)

        lets_see = Text("Let's see a visual proof!", font_size=36, color=YELLOW)
        lets_see.next_to(why_title, DOWN, buff=0.6)
        self.play(Write(lets_see))
        self.wait(2)

        self.play(FadeOut(why_title), FadeOut(lets_see))
        self.wait(0.5)

        # ═══════════════════════════════════════════════════════
        # PART 3: THE VISUAL PROOF
        # ═══════════════════════════════════════════════════════

        # First, show the triangle we'll be working with
        setup_text = Text("Here's our right triangle", font_size=30).to_edge(UP)
        self.play(Write(setup_text))
        self.wait(0.5)

        # Show a triangle in the center first
        demo_tri = Polygon(
            ORIGIN, RIGHT * a, UP * b,
            color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=3
        ).move_to(DOWN * 0.3)

        self.play(Create(demo_tri), run_time=1)

        # Label it with a, b, c
        demo_label_a = Text("a", font_size=32, color=A_COLOR).next_to(demo_tri, DOWN, buff=0.15)
        demo_label_b = Text("b", font_size=32, color=B_COLOR).next_to(demo_tri, LEFT, buff=0.15)
        demo_label_c = Text("c", font_size=32, color=C_COLOR)
        # Position c on the hypotenuse (between vertex 1 and vertex 2)
        demo_verts = demo_tri.get_vertices()
        demo_hyp_center = (demo_verts[1] + demo_verts[2]) / 2
        demo_label_c.move_to(demo_hyp_center + UR * 0.25)

        self.play(Write(demo_label_a), Write(demo_label_b), Write(demo_label_c))
        self.wait(1.5)

        self.play(FadeOut(setup_text))

        # Explain the plan
        plan_text = Text("We'll use 4 of these triangles", font_size=28).to_edge(UP)
        self.play(Write(plan_text))
        self.wait(1.5)

        plan_text2 = Text("to partially fill a square with side (a + b)", font_size=28).to_edge(UP)
        self.play(ReplacementTransform(plan_text, plan_text2))
        self.wait(1.5)

        # Fade the demo triangle
        self.play(FadeOut(demo_tri), FadeOut(demo_label_a), FadeOut(demo_label_b), FadeOut(demo_label_c), FadeOut(plan_text2))
        self.wait(0.5)

        # Now create the big square
        side = a + b
        big_square = Square(side_length=side, color=WHITE, stroke_width=3)
        big_square.move_to(DOWN * 0.3)

        bl = big_square.get_corner(DL)
        br = big_square.get_corner(DR)
        tr = big_square.get_corner(UR)
        tl = big_square.get_corner(UL)

        step1 = Text("Step 1: A square with side (a + b)", font_size=28).to_edge(UP)
        self.play(Write(step1))
        self.wait(0.5)
        self.play(Create(big_square), run_time=1.5)

        # Label the side
        side_label = Text("a + b", font_size=26).next_to(big_square, DOWN, buff=0.15)
        self.play(Write(side_label))
        self.wait(1.5)

        self.play(FadeOut(step1), FadeOut(side_label))
        self.wait(0.3)

        # ─────────────────────────────────────────────────────
        # Configuration 1: Four triangles with c² in center
        # ─────────────────────────────────────────────────────

        step2 = Text("Step 2: Place 4 a-b-c right triangles", font_size=28).to_edge(UP)
        self.play(Write(step2))
        self.wait(1)

        # Create all 4 triangles
        t1 = Polygon(bl, bl + RIGHT * a, bl + UP * b, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)
        t2 = Polygon(br, br + UP * a, br + LEFT * b, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)
        t3 = Polygon(tr, tr + LEFT * a, tr + DOWN * b, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)
        t4 = Polygon(tl, tl + DOWN * a, tl + RIGHT * b, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)

        # Create labels for ALL triangles - a, b on legs, c on hypotenuse
        # T1 labels
        t1_a = Text("a", font_size=18, color=A_COLOR).move_to(bl + RIGHT * a/2 + DOWN * 0.2)
        t1_b = Text("b", font_size=18, color=B_COLOR).move_to(bl + UP * b/2 + LEFT * 0.2)
        t1_c = Text("c", font_size=18, color=C_COLOR).move_to((bl + RIGHT * a + bl + UP * b) / 2 + UR * 0.15)

        # T2 labels
        t2_a = Text("a", font_size=18, color=A_COLOR).move_to(br + UP * a/2 + RIGHT * 0.2)
        t2_b = Text("b", font_size=18, color=B_COLOR).move_to(br + LEFT * b/2 + DOWN * 0.2)
        t2_c = Text("c", font_size=18, color=C_COLOR).move_to((br + UP * a + br + LEFT * b) / 2 + UL * 0.15)

        # T3 labels
        t3_a = Text("a", font_size=18, color=A_COLOR).move_to(tr + LEFT * a/2 + UP * 0.2)
        t3_b = Text("b", font_size=18, color=B_COLOR).move_to(tr + DOWN * b/2 + RIGHT * 0.2)
        t3_c = Text("c", font_size=18, color=C_COLOR).move_to((tr + LEFT * a + tr + DOWN * b) / 2 + DL * 0.15)

        # T4 labels
        t4_a = Text("a", font_size=18, color=A_COLOR).move_to(tl + DOWN * a/2 + LEFT * 0.2)
        t4_b = Text("b", font_size=18, color=B_COLOR).move_to(tl + RIGHT * b/2 + UP * 0.2)
        t4_c = Text("c", font_size=18, color=C_COLOR).move_to((tl + DOWN * a + tl + RIGHT * b) / 2 + DR * 0.15)

        all_labels = VGroup(t1_a, t1_b, t1_c, t2_a, t2_b, t2_c, t3_a, t3_b, t3_c, t4_a, t4_b, t4_c)

        # Animate triangles appearing
        self.play(FadeIn(t1), run_time=0.6)
        self.play(Write(t1_a), Write(t1_b), Write(t1_c), run_time=0.5)
        self.wait(0.3)

        self.play(FadeIn(t2), run_time=0.5)
        self.play(Write(t2_a), Write(t2_b), Write(t2_c), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(t3), run_time=0.5)
        self.play(Write(t3_a), Write(t3_b), Write(t3_c), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(t4), run_time=0.5)
        self.play(Write(t4_a), Write(t4_b), Write(t4_c), run_time=0.4)
        self.wait(1)

        self.play(FadeOut(step2))
        self.wait(0.5)

        # Highlight the center square
        step3 = Text("A square forms in the center", font_size=28).to_edge(UP)
        self.play(Write(step3))
        self.wait(0.5)

        center_verts = [bl + RIGHT * a, br + UP * a, tr + LEFT * a, tl + DOWN * a]
        center_square = Polygon(*center_verts, color=C_COLOR, fill_color=YELLOW_E, fill_opacity=0.5, stroke_width=3)

        self.play(Create(center_square), run_time=1)
        self.wait(0.5)

        self.play(FadeOut(step3))

        # Label center square as c² - each side is c (the hypotenuse)
        step3b = Text("It has area c²", font_size=28).to_edge(UP)
        self.play(Write(step3b))
        self.wait(0.5)

        c_sq_label = Text("c²", font_size=40, color=C_COLOR).move_to(center_square)
        self.play(Write(c_sq_label))
        self.wait(1.5)

        self.play(FadeOut(step3b))

        # Configuration 1 label
        config1_text = Text("Configuration 1", font_size=26).to_edge(UP)
        self.play(Write(config1_text))
        self.wait(2)

        # Fade center square highlight but keep triangles and labels
        self.play(FadeOut(center_square), FadeOut(c_sq_label), FadeOut(config1_text))
        self.wait(0.5)

        # ─────────────────────────────────────────────────────
        # Configuration 2: Rearrange to show a² and b²
        # ─────────────────────────────────────────────────────

        step4 = Text("Step 3: Rearrange the triangles", font_size=28).to_edge(UP)
        self.play(Write(step4))
        self.wait(1.5)

        # Fade out labels before moving triangles
        self.play(FadeOut(all_labels))
        self.wait(0.3)

        # Define target positions for Configuration 2
        # T1: stays at bottom-left (no change!)
        # T2: rotates and moves to complete bottom-left rectangle
        t2_target = Polygon(bl + UP * b, bl + RIGHT * a, bl + RIGHT * a + UP * b,
                           color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)
        # T3: rotates in place (swaps a and b legs)
        t3_target = Polygon(tr, tr + LEFT * b, tr + DOWN * a,
                           color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)
        # T4: rotates and moves to complete top-right rectangle
        t4_target = Polygon(tr + DOWN * a, tr + LEFT * b, tr + LEFT * b + DOWN * a,
                           color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7, stroke_width=2)

        # Animate the rearrangement with rotation paths!
        # t1 stays in place, t2/t3/t4 rotate and translate
        self.play(
            Transform(t2, t2_target, path_arc=PI),      # t2 flips 180° moving left
            Transform(t3, t3_target, path_arc=-PI/2),   # t3 rotates 90° in place
            Transform(t4, t4_target, path_arc=-PI),     # t4 flips 180° moving right
            run_time=3
        )
        self.wait(0.5)

        # Add a, b labels to the rearranged triangles
        # Left rectangle triangles (t1 and t2)
        t1_a_new = Text("a", font_size=18, color=A_COLOR).move_to(bl + RIGHT * a/2 + DOWN * 0.2)
        t1_b_new = Text("b", font_size=18, color=B_COLOR).move_to(bl + UP * b/2 + LEFT * 0.2)
        t2_a_new = Text("a", font_size=18, color=A_COLOR).move_to(bl + RIGHT * a + UP * b/2 + RIGHT * 0.2)
        t2_b_new = Text("b", font_size=18, color=B_COLOR).move_to(bl + RIGHT * a/2 + UP * b + UP * 0.2)

        # Right rectangle triangles (t3 and t4)
        t3_a_new = Text("a", font_size=18, color=A_COLOR).move_to(tr + DOWN * a/2 + RIGHT * 0.2)
        t3_b_new = Text("b", font_size=18, color=B_COLOR).move_to(tr + LEFT * b/2 + UP * 0.2)
        t4_a_new = Text("a", font_size=18, color=A_COLOR).move_to(tr + LEFT * b + DOWN * a/2 + LEFT * 0.2)
        t4_b_new = Text("b", font_size=18, color=B_COLOR).move_to(tr + LEFT * b/2 + DOWN * a + DOWN * 0.2)

        new_labels = VGroup(t1_a_new, t1_b_new, t2_a_new, t2_b_new, t3_a_new, t3_b_new, t4_a_new, t4_b_new)
        self.play(FadeIn(new_labels), run_time=0.8)
        self.wait(1)

        self.play(FadeOut(step4))
        self.wait(0.5)

        # Highlight the two squares with labels on their sides
        step5 = Text("Two squares appear!", font_size=28).to_edge(UP)
        self.play(Write(step5), FadeOut(new_labels))
        self.wait(1)

        # a² square in top-left
        a_square = Square(side_length=a, color=A_COLOR, fill_color=RED_E, fill_opacity=0.5, stroke_width=3)
        a_square.move_to(tl + RIGHT * a/2 + DOWN * a/2)

        # b² square in bottom-right
        b_square = Square(side_length=b, color=B_COLOR, fill_color=GREEN_E, fill_opacity=0.5, stroke_width=3)
        b_square.move_to(br + LEFT * b/2 + UP * b/2)

        self.play(Create(a_square), run_time=0.8)

        # Label a² square with side labels
        a_sq_label = Text("a²", font_size=32, color=A_COLOR).move_to(a_square)
        a_side_top = Text("a", font_size=20, color=A_COLOR).next_to(a_square, UP, buff=0.1)
        a_side_left = Text("a", font_size=20, color=A_COLOR).next_to(a_square, LEFT, buff=0.1)

        self.play(Write(a_sq_label), Write(a_side_top), Write(a_side_left))
        self.wait(0.5)

        self.play(Create(b_square), run_time=0.8)

        # Label b² square with side labels
        b_sq_label = Text("b²", font_size=32, color=B_COLOR).move_to(b_square)
        b_side_bottom = Text("b", font_size=20, color=B_COLOR).next_to(b_square, DOWN, buff=0.1)
        b_side_right = Text("b", font_size=20, color=B_COLOR).next_to(b_square, RIGHT, buff=0.1)

        self.play(Write(b_sq_label), Write(b_side_bottom), Write(b_side_right))
        self.wait(1.5)

        self.play(FadeOut(step5))

        # Configuration 2 label
        config2_text = Text("Configuration 2", font_size=26).to_edge(UP)
        self.play(Write(config2_text))
        self.wait(2)

        self.play(FadeOut(config2_text))
        self.wait(0.5)

        # ═══════════════════════════════════════════════════════
        # PART 4: SHOW BOTH SIDE BY SIDE
        # ═══════════════════════════════════════════════════════

        # Fade current view
        self.play(
            FadeOut(big_square), FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4),
            FadeOut(a_square), FadeOut(b_square),
            FadeOut(a_sq_label), FadeOut(b_sq_label),
            FadeOut(a_side_top), FadeOut(a_side_left),
            FadeOut(b_side_bottom), FadeOut(b_side_right)
        )
        self.wait(0.5)

        comparison_title = Text("Both use the same big square", font_size=28).to_edge(UP)
        self.play(Write(comparison_title))
        self.wait(1)

        # Create both configurations side by side
        s = 0.7  # scale factor - larger for better visibility

        # Config 1 (left)
        sq1 = Square(side_length=side * s, color=WHITE, stroke_width=2)
        sq1.move_to(LEFT * 2.8 + DOWN * 0.2)

        bl1 = sq1.get_corner(DL)
        br1 = sq1.get_corner(DR)
        tr1 = sq1.get_corner(UR)
        tl1 = sq1.get_corner(UL)

        t1_c1 = Polygon(bl1, bl1 + RIGHT * a * s, bl1 + UP * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t2_c1 = Polygon(br1, br1 + UP * a * s, br1 + LEFT * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t3_c1 = Polygon(tr1, tr1 + LEFT * a * s, tr1 + DOWN * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t4_c1 = Polygon(tl1, tl1 + DOWN * a * s, tl1 + RIGHT * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)

        center_c1 = Polygon(
            bl1 + RIGHT * a * s, br1 + UP * a * s, tr1 + LEFT * a * s, tl1 + DOWN * a * s,
            color=C_COLOR, fill_color=YELLOW_E, fill_opacity=0.5
        )
        c_label_c1 = Text("c²", font_size=36, color=C_COLOR).move_to(center_c1)

        config1_group = VGroup(sq1, t1_c1, t2_c1, t3_c1, t4_c1, center_c1, c_label_c1)

        # Config 2 (right)
        sq2 = Square(side_length=side * s, color=WHITE, stroke_width=2)
        sq2.move_to(RIGHT * 2.8 + DOWN * 0.2)

        bl2 = sq2.get_corner(DL)
        br2 = sq2.get_corner(DR)
        tr2 = sq2.get_corner(UR)
        tl2 = sq2.get_corner(UL)

        t1_c2 = Polygon(bl2, bl2 + RIGHT * a * s, bl2 + UP * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t2_c2 = Polygon(bl2 + UP * b * s, bl2 + RIGHT * a * s, bl2 + RIGHT * a * s + UP * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t3_c2 = Polygon(tr2, tr2 + LEFT * b * s, tr2 + DOWN * a * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t4_c2 = Polygon(tr2 + DOWN * a * s, tr2 + LEFT * b * s, tr2 + LEFT * b * s + DOWN * a * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)

        a_sq_c2 = Square(side_length=a * s, color=A_COLOR, fill_color=RED_E, fill_opacity=0.5)
        a_sq_c2.move_to(tl2 + RIGHT * a * s / 2 + DOWN * a * s / 2)
        a_label_c2 = Text("a²", font_size=28, color=A_COLOR).move_to(a_sq_c2)

        b_sq_c2 = Square(side_length=b * s, color=B_COLOR, fill_color=GREEN_E, fill_opacity=0.5)
        b_sq_c2.move_to(br2 + LEFT * b * s / 2 + UP * b * s / 2)
        b_label_c2 = Text("b²", font_size=28, color=B_COLOR).move_to(b_sq_c2)

        config2_group = VGroup(sq2, t1_c2, t2_c2, t3_c2, t4_c2, a_sq_c2, b_sq_c2, a_label_c2, b_label_c2)

        self.play(FadeIn(config1_group), FadeIn(config2_group), run_time=1.5)
        self.wait(1)

        self.play(FadeOut(comparison_title))

        # Show labels under each configuration
        label1 = Text("Configuration 1", font_size=20).next_to(sq1, DOWN, buff=0.25)
        label2 = Text("Configuration 2", font_size=20).next_to(sq2, DOWN, buff=0.25)
        self.play(Write(label1), Write(label2))
        self.wait(1)

        # Explain the key insight
        insight_text = Text("The area not covered by triangles", font_size=26).to_edge(UP)
        self.play(Write(insight_text))
        self.wait(1)

        insight_text2 = Text("must be the same in both!", font_size=26).to_edge(UP)
        self.play(ReplacementTransform(insight_text, insight_text2))
        self.wait(1)

        # Pulse/glow both regions simultaneously to show they're equal
        # First pulse - highlight both regions together
        self.play(
            Indicate(center_c1, color=WHITE, scale_factor=1.1),
            Indicate(a_sq_c2, color=WHITE, scale_factor=1.1),
            Indicate(b_sq_c2, color=WHITE, scale_factor=1.1),
            run_time=1.2
        )
        self.wait(0.3)

        # Second pulse for emphasis
        self.play(
            Indicate(center_c1, color=WHITE, scale_factor=1.1),
            Indicate(a_sq_c2, color=WHITE, scale_factor=1.1),
            Indicate(b_sq_c2, color=WHITE, scale_factor=1.1),
            run_time=1.2
        )
        self.wait(0.5)

        self.play(FadeOut(insight_text2))

        # Build equation: c² on left, pulsing with its region
        c2_eq = Text("c²", font_size=44, color=C_COLOR).next_to(label1, DOWN, buff=0.4)
        self.play(Write(c2_eq), Indicate(center_c1, color=C_COLOR, scale_factor=1.05))
        self.wait(0.3)

        # = sign
        equals = Text("=", font_size=44).move_to((c2_eq.get_center() + RIGHT * 2.8))
        self.play(Write(equals))
        self.wait(0.3)

        # a² + b² on right, pulsing with their regions
        ab2_eq = make_equation([("a²", A_COLOR), ("+", WHITE), ("b²", B_COLOR)], font_size=44)
        ab2_eq.next_to(label2, DOWN, buff=0.4)
        self.play(
            Write(ab2_eq),
            Indicate(a_sq_c2, color=A_COLOR, scale_factor=1.05),
            Indicate(b_sq_c2, color=B_COLOR, scale_factor=1.05)
        )
        self.wait(2)

        # ═══════════════════════════════════════════════════════
        # PART 5: CONCLUSION
        # ═══════════════════════════════════════════════════════

        self.play(
            FadeOut(config1_group), FadeOut(config2_group),
            FadeOut(label1), FadeOut(label2),
            FadeOut(c2_eq), FadeOut(ab2_eq), FadeOut(equals)
        )
        self.wait(0.5)

        # Final reveal
        therefore = Text("Therefore:", font_size=40).move_to(UP * 1.5)
        self.play(Write(therefore))
        self.wait(0.5)

        final_eq = make_equation([
            ("c²", C_COLOR), ("=", WHITE), ("a²", A_COLOR), ("+", WHITE), ("b²", B_COLOR)
        ], font_size=72)
        final_eq.move_to(ORIGIN)

        self.play(Write(final_eq), run_time=1.5)
        self.wait(1)

        box = SurroundingRectangle(final_eq, color=WHITE, buff=0.4, corner_radius=0.15)
        self.play(Create(box))
        self.wait(1)

        tada = Text("The Pythagorean Theorem!", font_size=36, color=GREEN)
        tada.next_to(box, DOWN, buff=0.5)
        self.play(Write(tada))
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)


class NumericExample(Scene):
    def construct(self):
        title = Text("Let's Check with Numbers", font_size=44).to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(1.5)

        subtitle = Text("The 3-4-5 triangle", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        self.wait(1.5)

        # Create triangle
        scale = 0.55
        a, b = 3 * scale, 4 * scale

        triangle = Polygon(
            ORIGIN, RIGHT * a, RIGHT * a + UP * b,
            color=BLUE, fill_color=BLUE_E, fill_opacity=0.5, stroke_width=3
        ).move_to(LEFT * 2.5 + DOWN * 0.3)

        self.play(Create(triangle), run_time=1)
        self.wait(0.3)

        # Add right angle marker
        tri_verts = triangle.get_vertices()
        ra_size = 0.18
        right_angle = VMobject(color=WHITE, stroke_width=2)
        right_angle.set_points_as_corners([
            tri_verts[1] + LEFT * ra_size,
            tri_verts[1] + LEFT * ra_size + UP * ra_size,
            tri_verts[1] + UP * ra_size
        ])
        self.play(Create(right_angle), run_time=0.5)
        self.wait(0.3)

        # Labels
        label_3 = Text("3", font_size=40, color=RED).next_to(triangle, DOWN, buff=0.15)
        label_4 = Text("4", font_size=40, color=GREEN).next_to(triangle, RIGHT, buff=0.15)
        hyp_center = (tri_verts[0] + tri_verts[2]) / 2
        label_5 = Text("5", font_size=40, color=YELLOW).move_to(hyp_center + UL * 0.35)

        self.play(Write(label_3))
        self.wait(0.5)
        self.play(Write(label_4))
        self.wait(0.5)
        self.play(Write(label_5))
        self.wait(1.5)

        # Calculation
        calc_x = RIGHT * 2.2

        line1 = make_equation([("c²", YELLOW), ("=", WHITE), ("a²", RED), ("+", WHITE), ("b²", GREEN)], font_size=40)
        line1.move_to(calc_x + UP * 1.2)
        self.play(Write(line1))
        self.wait(1.5)

        line2 = make_equation([("5²", YELLOW), ("=", WHITE), ("3²", RED), ("+", WHITE), ("4²", GREEN)], font_size=40)
        line2.move_to(calc_x + UP * 0.3)
        self.play(Write(line2))
        self.wait(1.5)

        line3 = make_equation([("25", WHITE), ("=", WHITE), ("9", WHITE), ("+", WHITE), ("16", WHITE)], font_size=40)
        line3.move_to(calc_x + DOWN * 0.5)
        self.play(Write(line3))
        self.wait(1.5)

        line4 = make_equation([("25", GREEN), ("=", GREEN), ("25", GREEN)], font_size=44)
        check = Text("✓", font_size=48, color=GREEN)
        line4.move_to(calc_x + DOWN * 1.4)
        check.next_to(line4, RIGHT, buff=0.2)
        self.play(Write(line4), Write(check))
        self.wait(1)

        works = Text("It works!", font_size=40, color=YELLOW)
        works.move_to(DOWN * 2.5)
        self.play(Write(works))
        self.wait(2.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ConfigurationDiagrams(Scene):
    """Static image of both configurations for slides"""
    def construct(self):
        a = 1.2
        b = 1.6
        side = a + b
        s = 0.65

        TRI_COLOR = BLUE
        TRI_FILL = BLUE_E

        # Config 1
        sq1 = Square(side_length=side * s, color=WHITE, stroke_width=2)
        sq1.move_to(LEFT * 3)

        bl1 = sq1.get_corner(DL)
        br1 = sq1.get_corner(DR)
        tr1 = sq1.get_corner(UR)
        tl1 = sq1.get_corner(UL)

        t1_c1 = Polygon(bl1, bl1 + RIGHT * a * s, bl1 + UP * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t2_c1 = Polygon(br1, br1 + UP * a * s, br1 + LEFT * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t3_c1 = Polygon(tr1, tr1 + LEFT * a * s, tr1 + DOWN * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t4_c1 = Polygon(tl1, tl1 + DOWN * a * s, tl1 + RIGHT * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)

        center_c1 = Polygon(
            bl1 + RIGHT * a * s, br1 + UP * a * s, tr1 + LEFT * a * s, tl1 + DOWN * a * s,
            color=YELLOW, fill_color=YELLOW_E, fill_opacity=0.5
        )
        c_label = Text("c²", font_size=32, color=YELLOW).move_to(center_c1)

        label1 = Text("Configuration 1", font_size=22).next_to(sq1, DOWN, buff=0.3)

        # Config 2
        sq2 = Square(side_length=side * s, color=WHITE, stroke_width=2)
        sq2.move_to(RIGHT * 3)

        bl2 = sq2.get_corner(DL)
        br2 = sq2.get_corner(DR)
        tr2 = sq2.get_corner(UR)
        tl2 = sq2.get_corner(UL)

        t1_c2 = Polygon(bl2, bl2 + RIGHT * a * s, bl2 + UP * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t2_c2 = Polygon(bl2 + UP * b * s, bl2 + RIGHT * a * s, bl2 + RIGHT * a * s + UP * b * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t3_c2 = Polygon(tr2, tr2 + LEFT * b * s, tr2 + DOWN * a * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)
        t4_c2 = Polygon(tr2 + DOWN * a * s, tr2 + LEFT * b * s, tr2 + LEFT * b * s + DOWN * a * s, color=TRI_COLOR, fill_color=TRI_FILL, fill_opacity=0.7)

        a_sq = Square(side_length=a * s, color=RED, fill_color=RED_E, fill_opacity=0.5)
        a_sq.move_to(tl2 + RIGHT * a * s / 2 + DOWN * a * s / 2)
        a_label = Text("a²", font_size=28, color=RED).move_to(a_sq)

        b_sq = Square(side_length=b * s, color=GREEN, fill_color=GREEN_E, fill_opacity=0.5)
        b_sq.move_to(br2 + LEFT * b * s / 2 + UP * b * s / 2)
        b_label = Text("b²", font_size=28, color=GREEN).move_to(b_sq)

        label2 = Text("Configuration 2", font_size=22).next_to(sq2, DOWN, buff=0.3)

        # Equals
        eq = Text("=", font_size=48).move_to(ORIGIN)

        # Title
        title = Text("Both use 4 identical blue triangles", font_size=26, color=GRAY).to_edge(UP)

        self.add(
            sq1, t1_c1, t2_c1, t3_c1, t4_c1, center_c1, c_label, label1,
            sq2, t1_c2, t2_c2, t3_c2, t4_c2, a_sq, b_sq, a_label, b_label, label2,
            eq, title
        )
