from tkinter.constants import RIGHT
from turtle import Turtle,Screen
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT= 0
DOWN =270
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
import time
class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
    # screen = Screen()
    def make_snake(self):
        # self.segments = []
        for position in STARTING_POSITIONS:
            self.inc_snake(position)

    def inc_snake(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.inc_snake(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)



