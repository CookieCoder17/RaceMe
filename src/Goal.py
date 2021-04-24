import turtle
from turtle import *


class Goal(turtle.Turtle):
    '''
        Turtle Object Class for the goal's of each racer in the RaceMe game. 
        Defined are the common attributes among all of the goals.
    '''

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)
