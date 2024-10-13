from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGNMENT, font= FONT)
        # self.hideturtle()
        # self.write((0,270),False)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", move=False, align= ALIGNMENT, font= FONT)

    def inc_score(self):
        self.score += 1;
        self.clear()
        self.write(arg=f"Score = {self.score}", move=False, align='Center', font=('Arial', 24, 'normal'))
