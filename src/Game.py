import turtle
import os
from turtle import *
from random import random, choice, randrange
from Goal import Goal
from Racer import Turtle
from LeaderBoard import LeaderBoard
import math


class Game:
    '''
        The second segment and the bulk of the RaceMe Game. All of the game mechanics occurs 
        here. Programmed using the turtle module, the program first opens a new screen and sets 
        up the racing arena based on the number of racers added in the pregame.The script calls 
        both the Goal and Racer Classes. Using the ontimer, the Script runnes a series of races 
        and prompts the winner of each with an arithmetic challenge. If answered correctly, the 
        player is awarded points. After the rounds are over, the Classes is then closed, and the 
        leaderboard class is called
    '''

    def __init__(self, p, m, r):
        player_list = p
        self.rounds_left = r  # Keeps track of the number of rounds remaining
        self.player_scores = dict()  # Keeps track of the player's scores
        self.max = m
        self.s = turtle.Screen()
        self.setScreen()
        # Returns the positions for the goals
        pos = self.set_Race((len(player_list)))
        self.add_Racers(player_list, pos)
        self.s.tracer(0)  # Turns off the turtle's animation
        while True:
            # Timer that calls the game loop ever 200 milliseconds
            self.s.ontimer(self.Activity(), 200)

    def setScreen(self):
        # Fix the screen's coordinates
        self.s.setworldcoordinates(0, 0, 720, 520)
        self.s.bgcolor('silver')
        self.s.title('Race Me!')

    def generate_Challenge(self, max_num):
        '''
            Returns a string equation from 2 randomly generated operands and a random operator
        '''
        a = str(randrange(2, max_num))  # max int for the first integer
        b = str(randrange(2, max_num))  # max int for the second integer
        oper = choice(['+', '-', '*'])  # You may add other operations
        equ = str(a + '  ' + oper + '  ' + b)
        return equ

    def check(self, a, b):
        '''
        Returns a boolean value of whether the two answers match
        '''
        if a == b:
            return True
        else:
            return False

    def set_Race(self, lines):
        '''
            Takes in the number of lines to be created for the 
            turtle racers. Returns a list of integer postions 
            for the x coordinates of the lines
        '''
        positions = []  # List of the positions of the lines
        track_maker = turtle.Turtle()
        track_maker.hideturtle()
        track_maker.pen(fillcolor="white", pencolor="white", pensize=40)
        h = self.s.window_height()
        w = self.s.window_width()
        pos = w/(lines+1)  # Divides the lines across the screen correctly
        track_maker.left(90)
        for i in range(1, lines+1):
            track_maker.penup()
            track_maker.setpos(pos*i, 0)
            track_maker.pendown()
            track_maker.fd(h)
            positions.append(pos*i)  # Appens the new position
        return positions  # Retuns the list

    def add_Racers(self, players, positions):
        '''
            Takes in players; a dictionary of the players.
            positions, a list of integer postions for the 
            turtle's track lines
        '''
        self.racers = []  # Keeps track of the turtles that are created to be racers
        with open('src/score.txt', 'w') as edit:  # Creates the stats sheet
            i = 0  # Match the positions with the players
            for player in players.keys():
                new_turtle = Turtle(player, players[player])
                new_turtle.setpos(positions[i], 30)
                new_turtle.write(new_turtle.name, font=("Verdana", 8, "bold"),
                                 align='center', move=False)
                new_turtle.showturtle()
                new_goal = Goal()
                new_goal.color(new_turtle.col)
                new_goal.setpos(positions[i], self.s.window_height()-50)
                self.racers.append(new_turtle)  # Append the new racer
                self.player_scores[player] = 0
                # Write the turtle's name in the stats sheet
                edit.write(player + ' 0 \n')
                i += 1  # Increment the index for the position

    def turtle_move(self):
        '''
            Checks whether their are any rounds remaining, if so, the turtle moves 
            forward for a random distance until one the turtles reach their goal. 
            The fin_round is then called with the winner as the parameter. If their 
            are no more rounds left, the game_over function is called.
        '''
        if self.rounds_left > 0:  # Checks whether their are rounds remaining
            for turtle in self.racers:
                if turtle.heading() == 90:  # Only for the turtle's racing
                    if turtle.ycor()+15 <= self.s.window_height()-50:
                        dis = int(random() * 25)  # Generate a random integer
                        turtle.fd(dis)
                    else:
                        self.fin_round(turtle.name)  # The winner's name
        else:
            self.game_over()

    def fin_round(self, name):
        self.rounds_left -= 1  # Decerement the number of rounds
        for turtle in self.racers:  # Position the turtles back
            turtle.hideturtle()
            turtle.sety(30)
            turtle.showturtle()
        question = self.generate_Challenge(self.max)
        answer = eval(question)  # Evalutes the equation
        score = self.check(answer, self.s.numinput(
            'Congrats! Here is your challenge', 'Solve: ' + question + ' = '))
        if score:
            with open('src/score.txt', 'w+') as editor:
                # Add points if the winner answered correctly
                self.player_scores[name] += 5
                for i in self.player_scores.items():  # Edit the score sheet
                    editor.write(i[0] + ' ' + str(i[1]) + '\n')
        else:
            return

    def game_over(self):
        '''
            The Game screen is closed and the Leaderboard class is called with a 
            dictionary of the player's final stats as the parameter
        '''
        turtle.bye()
        LeaderBoard(self.player_scores)

    def Activity(self):
        self.s.update()  # Perform a TurtleScreen update.
        self.turtle_move()  # Calls the method main game loop
