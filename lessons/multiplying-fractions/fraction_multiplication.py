from manim import *


class HalfOfAThird(Scene):
    """
    Perspective 1: 1/2 × 1/3 means "half of one-third"
    Shows: unit square → divide into thirds → highlight one third →
           cut in half → arrive at 1/6
    """
    def construct(self):
        # Colors
        THIRD_COLOR = "#ff6b6b"  # Red for the 1/3
        PRODUCT_COLOR = "#9775fa"  # Purple for the result
        GRID_COLOR = "#868e96"  # Gray for grid lines

        # Unit square - size 3 for clean divisions
        square_size = 3
        square = Square(side_length=square_size, color=WHITE, stroke_width=3)
        square.move_to(ORIGIN)

        # Get corners for reference
        bl = square.get_corner(DL)
        br = square.get_corner(DR)
        tr = square.get_corner(UR)
        tl = square.get_corner(UL)

        # ═══════════════════════════════════════════════════════
        # STEP 1: Show the unit square
        # ═══════════════════════════════════════════════════════

        self.play(Create(square), run_time=1)

        label_one = Text("1", font_size=36, color=WHITE).move_to(square)
        self.play(Write(label_one))
        self.wait(1)
        self.play(FadeOut(label_one))
        self.wait(0.5)

        # ═══════════════════════════════════════════════════════
        # STEP 2: Divide into thirds (horizontal lines)
        # ═══════════════════════════════════════════════════════

        third = square_size / 3

        # Horizontal lines at 1/3 and 2/3 from bottom
        h_line1 = Line(bl + UP * third, br + UP * third, color=GRID_COLOR, stroke_width=2)
        h_line2 = Line(bl + UP * 2 * third, br + UP * 2 * third, color=GRID_COLOR, stroke_width=2)

        self.play(Create(h_line1), Create(h_line2), run_time=1)
        self.wait(0.5)

        # Label: "Three thirds"
        thirds_label = Text("Three equal parts", font_size=28, color=GRAY).to_edge(UP)
        self.play(Write(thirds_label))
        self.wait(1)
        self.play(FadeOut(thirds_label))

        # ═══════════════════════════════════════════════════════
        # STEP 3: Highlight one third (top strip)
        # ═══════════════════════════════════════════════════════

        # Top third strip
        top_third = Rectangle(
            width=square_size,
            height=third,
            color=THIRD_COLOR,
            fill_color=THIRD_COLOR,
            fill_opacity=0.5,
            stroke_width=2
        )
        top_third.move_to(tl + DOWN * third/2 + RIGHT * square_size/2)

        self.play(FadeIn(top_third), run_time=0.8)

        third_label = Text("This is 1/3", font_size=32, color=THIRD_COLOR).to_edge(UP)
        self.play(Write(third_label))
        self.wait(1.5)
        self.play(FadeOut(third_label))

        # ═══════════════════════════════════════════════════════
        # STEP 4: Cut in half (vertical line)
        # ═══════════════════════════════════════════════════════

        half_label = Text("Now take half of it", font_size=28, color=GRAY).to_edge(UP)
        self.play(Write(half_label))
        self.wait(0.5)

        # Vertical line at midpoint (top to bottom)
        v_line = Line(tl + RIGHT * square_size/2, bl + RIGHT * square_size/2, color=GRID_COLOR, stroke_width=2)
        self.play(Create(v_line), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(half_label))

        # ═══════════════════════════════════════════════════════
        # STEP 5: Highlight half of the third (purple)
        # ═══════════════════════════════════════════════════════

        # Left half of top third
        half_of_third = Rectangle(
            width=square_size/2,
            height=third,
            color=PRODUCT_COLOR,
            fill_color=PRODUCT_COLOR,
            fill_opacity=0.7,
            stroke_width=3
        )
        half_of_third.move_to(tl + DOWN * third/2 + RIGHT * square_size/4)

        # Fade out the full third, show the half
        self.play(FadeOut(top_third), FadeIn(half_of_third), run_time=0.8)

        result_label = Text("Half of one-third", font_size=32, color=PRODUCT_COLOR).to_edge(UP)
        self.play(Write(result_label))
        self.wait(1.5)
        self.play(FadeOut(result_label))

        # ═══════════════════════════════════════════════════════
        # STEP 6: Ask the question (stays visible)
        # ═══════════════════════════════════════════════════════

        # "How much of the square is this?" with "this" in purple
        question = MarkupText(
            f'How much of the square is <span foreground="{PRODUCT_COLOR}">this</span>?',
            font_size=28,
            color=GRAY
        )
        question.to_edge(UP)

        self.play(Write(question))
        self.wait(1)

        # ═══════════════════════════════════════════════════════
        # STEP 7: Highlight that our piece is 1 of 6
        # ═══════════════════════════════════════════════════════

        # Make the purple piece pulse
        self.play(Indicate(half_of_third, color=WHITE, scale_factor=1.05))

        # Show "1/6" below the question
        answer = Text("1/6", font_size=36, color=PRODUCT_COLOR)
        answer.next_to(question, DOWN, buff=0.4)
        self.play(FadeIn(answer))
        self.wait(1.5)

        # ═══════════════════════════════════════════════════════
        # STEP 8: Show the equation
        # ═══════════════════════════════════════════════════════

        # Equation: 1/2 of 1/3 = 1/6
        equation = Text("1/2 of 1/3 = 1/6", font_size=44, color=WHITE)
        equation.to_edge(DOWN, buff=1.2)

        self.play(Write(equation))
        self.wait(0.5)

        # Box the answer
        box = SurroundingRectangle(equation, color=PRODUCT_COLOR, buff=0.2, corner_radius=0.1)
        self.play(Create(box))
        self.wait(2)

        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)


class AreaOfRectangle(Scene):
    """
    Perspective 2: 1/2 × 1/3 means "area of a rectangle with sides 1/2 and 1/3"
    Shows: unit square → draw rectangle → "how many fit?" → grid reveals it's 1/6
    """
    def construct(self):
        # Colors
        RECT_COLOR = "#4dabf7"  # Blue for the rectangle
        PRODUCT_COLOR = "#9775fa"  # Purple for the final highlight
        GRID_COLOR = "#868e96"  # Gray for grid lines

        # Unit square - size 3 for clean divisions
        square_size = 3
        square = Square(side_length=square_size, color=WHITE, stroke_width=3)
        square.move_to(ORIGIN)

        # Get corners
        bl = square.get_corner(DL)
        br = square.get_corner(DR)
        tr = square.get_corner(UR)
        tl = square.get_corner(UL)

        # ═══════════════════════════════════════════════════════
        # STEP 1: Show the unit square
        # ═══════════════════════════════════════════════════════

        self.play(Create(square), run_time=1)

        # Label sides as 1
        side_bottom = Text("1", font_size=28, color=WHITE).next_to(square, DOWN, buff=0.15)
        side_left = Text("1", font_size=28, color=WHITE).next_to(square, LEFT, buff=0.15)

        self.play(Write(side_bottom), Write(side_left))
        self.wait(0.5)

        area_label = Text("Area = 1", font_size=32, color=GRAY).to_edge(UP)
        self.play(Write(area_label))
        self.wait(1)
        self.play(FadeOut(area_label), FadeOut(side_bottom), FadeOut(side_left))

        # ═══════════════════════════════════════════════════════
        # STEP 2: Draw the rectangle (1/2 by 1/3) - TOP LEFT
        # ═══════════════════════════════════════════════════════

        rect_width = square_size / 2
        rect_height = square_size / 3

        # Rectangle anchored at top-left (matching Video 1)
        product_rect = Rectangle(
            width=rect_width,
            height=rect_height,
            color=RECT_COLOR,
            fill_color=RECT_COLOR,
            fill_opacity=0.6,
            stroke_width=3
        )
        product_rect.move_to(tl + RIGHT * rect_width/2 + DOWN * rect_height/2)

        self.play(GrowFromPoint(product_rect, tl), run_time=1.2)

        # Label the sides
        label_half = Text("1/2", font_size=28, color=RECT_COLOR)
        label_half.next_to(product_rect, UP, buff=0.1)

        label_third = Text("1/3", font_size=28, color=RECT_COLOR)
        label_third.next_to(product_rect, LEFT, buff=0.1)

        self.play(Write(label_half), Write(label_third))
        self.wait(1)

        # ═══════════════════════════════════════════════════════
        # STEP 3: Ask the question (stays visible)
        # ═══════════════════════════════════════════════════════

        # "What's the area of this rectangle?" with "rectangle" in blue
        question_part1 = Text("What's the area of this ", font_size=28, color=GRAY)
        question_part2 = Text("rectangle", font_size=28, color=RECT_COLOR)
        question_part3 = Text("?", font_size=28, color=GRAY)
        question = VGroup(question_part1, question_part2, question_part3).arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        question.to_edge(UP)

        self.play(Write(question))
        self.wait(1)

        # ═══════════════════════════════════════════════════════
        # STEP 4: Build the grid (question stays visible)
        # ═══════════════════════════════════════════════════════

        # Vertical line at 1/2 (top to bottom)
        v_line = Line(tl + RIGHT * square_size/2, bl + RIGHT * square_size/2, color=GRID_COLOR, stroke_width=2)
        self.play(Create(v_line), run_time=0.8)
        self.wait(0.5)

        # Horizontal lines at 1/3 and 2/3
        third = square_size / 3
        h_line1 = Line(bl + UP * third, br + UP * third, color=GRID_COLOR, stroke_width=2)
        h_line2 = Line(bl + UP * 2 * third, br + UP * 2 * third, color=GRID_COLOR, stroke_width=2)
        self.play(Create(h_line1), Create(h_line2), run_time=0.8)
        self.wait(1)

        # ═══════════════════════════════════════════════════════
        # STEP 5: Highlight the rectangle and reveal answer
        # ═══════════════════════════════════════════════════════

        # Pulse the rectangle
        self.play(Indicate(product_rect, color=WHITE, scale_factor=1.05))

        # Change to purple to match perspective 1
        product_rect_purple = Rectangle(
            width=rect_width,
            height=rect_height,
            color=PRODUCT_COLOR,
            fill_color=PRODUCT_COLOR,
            fill_opacity=0.7,
            stroke_width=3
        )
        product_rect_purple.move_to(tl + RIGHT * rect_width/2 + DOWN * rect_height/2)

        self.play(Transform(product_rect, product_rect_purple))
        self.wait(0.5)

        # ═══════════════════════════════════════════════════════
        # STEP 6: Show the answer
        # ═══════════════════════════════════════════════════════

        # Show "Area = 1/6" below the question (keep labels visible)
        answer = Text("Area = 1/6", font_size=36, color=PRODUCT_COLOR)
        answer.next_to(question, DOWN, buff=0.4)
        self.play(FadeIn(answer))
        self.wait(1.5)

        # Bring it full circle - connect back to multiplication
        equation = Text("1/2 × 1/3 = 1/6", font_size=44, color=WHITE)
        equation.to_edge(DOWN, buff=1.2)

        self.play(Write(equation))
        self.wait(0.5)

        box = SurroundingRectangle(equation, color=PRODUCT_COLOR, buff=0.2, corner_radius=0.1)
        self.play(Create(box))
        self.wait(2)

        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
