from manim import *

class Pitch(Scene):
    def construct(self):
        sq = Square(side_length=3, stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.75)
        self.play(Create(sq), run_time=3)
        self.wait()
