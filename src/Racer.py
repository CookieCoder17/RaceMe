import turtle
from turtle import *


class Turtle(turtle.Turtle):
    '''
        Turtle Object Class for the each of the player's turtles. Defined are the common 
        attributes among all of the racer turtles. The Turtle Class takes in a name and a
        color when instantiated. 
    '''

    def __init__(self, name, color):
        turtle.Turtle.__init__(self)
        self.name = name
        self.col = color
        self.hideturtle()
        self.color(self.col)
        self.penup()
        self.shape('turtle')
        self.shapesize(1)
        self.left(90)
