'''
SNAKE GAME
break into 7 problems
1. create snake body
2. move the snake
3. how to control snake
4. detect collison and food placement on screen at roandom
5. keep track of score and
6. when game to end
7. other collison rules of game end
'''

import time
import turtle
from turtle import Screen, Turtle
starting_positions= [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    MOVE_DISTANCE = 20
    HEAD_UP=90
    HEAD_DOWN=270
    HEAD_LEFT=180
    HEAD_RIGHT=0

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]


    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(self.MOVE_DISTANCE)


    def up(self):
        if self.head.heading()!= self.HEAD_DOWN:
            self.head.setheading(self.HEAD_UP)

    def down(self):
        if self.head.heading() != self.HEAD_UP:
            self.head.setheading(self.HEAD_DOWN)

    def left(self):
        if self.head.heading() != self.HEAD_RIGHT:
            self.head.setheading(self.HEAD_LEFT)

    def right(self):
        if self.head.heading() != self.HEAD_LEFT:
            self.head.setheading(self.HEAD_RIGHT)