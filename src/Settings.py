import os
import tkinter as tk
from tkinter import colorchooser, simpledialog, Label
from Game import Turtle, Goal, Game


class Settings:
    '''
        As the first segment in the RaceMe game, the Settings Class acts as the 
        pregame. Programmed using Tkinter, the GUI script will allow the user to 
        add and remove players by defining a name and color for each. The player 
        may also set the Difficulty of the arithmetic challenges and the number 
        of rounds. When done, the player may press 'Start Game' to close the 
        pregame and start to play!
    '''

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)  # Disable resizing
        self.root.title('RaceMe')
        self.players = dict()  # Keeps track of the players and their colors
        # Boolean for restricting the user to only undo the player recently added
        self.undo_ab = False
        self.max_num = 50  # Default Max Integer
        self.rounds = 3  # Default Number of Rounds
        self.setCanvas()
        self.setFrame()
        self.activeButtons()
        self.root.mainloop()

    def setCanvas(self):
        self.canvas = tk.Canvas(self.root, height=480,
                                width=320, bg='black')  # Canvas
        self.canvas.pack()

    def setFrame(self):
        self.frame = tk.Frame(self.root, bg='light blue')  # Frame
        self.frame.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.05)

    def activeButtons(self):
        # For adding Players
        addPlayer = tk.Button(self.root, text='Add Player', bg='light blue',
                              fg='black', width=11, command=self.add_player).place(x=20, y=380)
        # For removing the recently added player
        undo = tk.Button(self.root, text='Undo Player', bg='light blue',
                         fg='black', width=11, command=self.undo_player).place(x=20, y=420)
        # For Starting the game
        startGame = tk.Button(self.root, text='Start Game',
                              bg='light blue', fg='black', width=11, command=self.start_game).place(x=220, y=400)
        # For setting the difficulty
        numRange = tk.Button(self.root, text='Difficulty', bg='light blue',
                             fg='black', width=11, command=self.set_diff).place(x=120, y=420)
        # For setting the number of rounds in the race
        numRounds = tk.Button(self.root, text='Rounds', bg='light blue',
                              fg='black', width=11, command=self.num_rounds).place(x=120, y=380)

    def add_player(self):
        player_name = simpledialog.askstring(
            'Player Name', "Input the player's name")
        if player_name == "":  # Incase the user clicks cancel
            return
        else:
            # Calls the choose_color function
            color = self.choose_color(player_name)
            # Adds a new player to the dictionary
            self.players[player_name] = color
            self.text = Label(self.frame, text=player_name,
                              bg='light blue', font='Helvetica 12 bold')
            self.text.pack(pady=1)
            self.undo_ab = True  # Allow the user to remove the recently added player

    def undo_player(self):
        if(self.undo_ab):
            try:
                self.players.popitem()  # Remove the player from the dictionary
                self.text.destroy()  # Remove the player's label from the screen's list
                self.undo_ab = False  # Disable the user's ability to remove
            except KeyError:
                return
        else:
            return

    def choose_color(self, name):
        '''
            Returns the hexadecimal code of  the choosen color
        '''
        color_code = colorchooser.askcolor(title='Choose color for ' + name)
        return color_code[1]

    def set_diff(self):
        self.max_num = int(simpledialog.askstring(
            'Set Difficulty', 'Input the Maximum integer to be quized on!'))

    def num_rounds(self):
        self.rounds = int(simpledialog.askstring(
            'Rounds', 'Input the number of rounds in the session!'))

    def start_game(self):
        '''
            Closes the Settings and opens the an instance of the Game Class.
            Passes in the dictionary of players, the difficulty, and the number
            of rounds.
        '''
        self.root.destroy()
        Game(self.players, self.max_num, self.rounds)
