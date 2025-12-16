import tkinter as tk
import random

class myGUI:
    #Initializes the GUI 
    def __init__(self):
        self.__game = FishingGame()

        self.__main_window = tk.Tk()
        self.__main_window.title("Also not repurposed code")
        self.__main_window.geometry("600x400")
        
        #Making a menu bar
        self.__menu_bar = tk.Menu(self.__main_window)
        self.__main_window.config(menu = self.__menu_bar)

        #Making game menu
        self.__game_menu = tk.Menu(self.__menu_bar)
        self.__menu_bar.add_cascade(label = "Game", menu = self.__game_menu)
        self.__game_menu.add_command(label = "Start New Game", command = self.start_game)
        self.__game_menu.add_separator()
        self.__game_menu.add_command(label = "Reset the Game", command = self.reset_game)
        self.__game_menu.add_command(label = "End Game", command = self.end_game)

        #Making the help menu
        self.__help_menu = tk.Menu(self.__menu_bar)
        self.__menu_bar.add_cascade(label = "Help", menu = self.__help_menu)
        self.__help_menu.add_command(label = "Instructions", command = self.show_instructions)

        #Making something to display the player's status
        self.__fishLabel = tk.Label(self.__main_window, text = "Welcome to Muscle Music")
        self.__fishLabel.pack(pady = 20)

        #Making Reel Rod Button and points tracker and label
        self.__mid_frame = tk.Frame(self.__main_window)
        self.__reel_rod = tk.Button(self.__mid_frame, text = "Play Note", command = self.reel_rod)
        self.__reel_rod.pack(side= "left", padx= 20, pady = 20)
        self.__points = 0
        self.__mid_frame.pack()
        
    #Runs the start function in fishing game
    def start_game(self):
        self.__game.start_game()
        self.__fishLabel.config(text = "Game has started")

    #Runs the cast reel function in fishing game
    def cast_the_line(self):
        if self.__game.get_active():
            self.__game.cast_the_line()
        else:
            self.__fishLabel.config(text = f"You need to start a new game first!")

    #Runs the end game function in fishing game
    def end_game(self):
        self.__game.end_game()
        self.__main_window.destroy()

    #Runs the reel rod function in fishing game and shows fish
    def reel_rod(self):
        self.__game.set_fish()
        shape = self.__game.get_fish()
        self.__fishLabel.config(text = f"{shape}")

            
            
    #Causes points to reset and displays that the game has been restarted
    def reset_game (self):
        self.__points = 0
        self.__points_label.config(text = f"Points: {self.__points}")
        self.__game.reset_game()
        self.__fishLabel.config(text = f"Game has been reset!")

    #Instructions are set to fish label
    def show_instructions(self):
        instructions = "Welcome to the game. Use the game menu to start a new game, \ncast the fishing line, then reel in the rod, and end the game"
        self.__fishLabel.config(text = instructions)

class FishingGame:
    #Initializes fishing game
    def __init__(self):
        self.__casted = False

        #creates point tracker
        self.__point = 0
        
        #track whether the game is active or not
        self.game_active = False
        
    #Moves the turtle fishing_line down and sets casted to true 
    def cast_the_line(self):
        self.__casted = True

    #Sets the sprite of the fish and records the name of the fish as well as the points
    def set_fish(self):
        self.__fish_num = random.randint(1,100)
        if self.__fish_num <= 20:
            self.__fish_shape = "A"
            self.__point = 10
        elif self.__fish_num <= 40:
            self.__fish_shape = "B"
            self.__point = 10
        elif self.__fish_num <= 55:
            self.__fish_shape = "C"
            self.__point = 25
        elif self.__fish_num <= 70:
            self.__fish_shape = "D"
            self.__point = 25
        elif self.__fish_num <= 85:
            self.__fish_shape = "E"
            self.__point = 30
        elif self.__fish_num <= 92:
            self.__fish_shape = "F"
            self.__point = 50
        else:
            self.__fish_shape = "G"
            self.__point = 50


    #reels in the rod with a fish and determines whether or not line can be reeled
    def reel_the_line(self):
        self.__casted = False

            
    #Returns the shape of the fish to be printed in fishLabel 
    def get_fish(self):
        return self.__fish_shape
    #Returns the points of the fish to be printed in points_label 
    def get_points(self):
        return self.__point
    #Returns the points of the fish to be printed in points_label 
    def get_casted(self):
        return self.__casted
    def get_active(self):
        return self.game_active
    
    #Sets game_active as true and prints the game started   
    def start_game(self):
        self.game_active = True
        print("A new game has started")

    #Clears the points and reels in line with no fish 
    def reset_game(self):
        self.__casted = False
        
    #Sets game active as false and destroies the GUI and turtle while printing Game over!
    def end_game(self):
        self.game_active = False
        print("Game Over!")
        

#creates the game 
def main():
    myGame = myGUI()
   
main()
