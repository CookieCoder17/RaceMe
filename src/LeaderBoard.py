import tkinter as tk
from tkinter import Label, Canvas, Frame
from random import random


class LeaderBoard:
    '''
        Programmed using Tkinter, the script displays a leaderboard of 
        the players and their scores. The script takes in a dictionary 
        of players and their scores, sorts it, and displays it in a 
        Tkinter GUI.
    '''

    def __init__(self, scores):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title('LeaderBoard')
        self.player_scores = scores  # The players' scores
        self.setCanvas()
        self.setFrame()
        self.sorting_scores()
        self.root.mainloop()

    def setCanvas(self):
        self.canvas = Canvas(self.root, height=500, width=350, bg='black')
        self.canvas.pack()

    def setFrame(self):
        self.frame = Frame(self.root, bg='black')
        self.frame.place(relwidth=1, relheight=0.7)

    def sorting_scores(self):
        i = 1  # Keeps track of the placing in
        # Sorts the values of in the dict
        sorted_scores = sorted(self.player_scores.values(), reverse=True)
        for player in self.player_scores.items():
            player_name = list(self.player_scores.keys())[list(
                self.player_scores.values()).index(sorted_scores[i-1])]  # Retrives the player's name through their scores
            TEXT = str('#' + str(i) + '     ' + player_name +
                       '      ' + str(sorted_scores[i-1]))
            # Randomizes the player's score after written to avoid repition
            self.player_scores[player_name] = (random()*10000)
            if i % 2 == 0:
                BG = '#480091'
            else:
                BG = '#6000bf'
            text = Label(self.frame, text=TEXT, bg=BG,
                         font='Helvetica 25 bold')
            text.pack(pady=1)
            i += 1  # Increment the index
