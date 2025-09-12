"""
  Name: GIU_Dice_Roller
  Created by: Owen Graham
  Created: 
  Purpose: Roll a dice as its own little Gui window
"""

# import tkinter for the Gui
import tkinter as tk


# create a function for the dice rolling
def roll_dice(side):
    pass

# Create the individual window for future use ( will be moved later. )
root = tk.Tk()

# making a label.
label = tk.Label(root, text="Dice Roll!", font=("Arial", 14))
label.pack(pady=20)

roll_Button = tk.Button(root, text="Roll Dice", width=20, command=lambda: roll_dice("Roll!")) # defining a button for the GUI
roll_Button.place(x=100, y=175) # making it so the program displays the button where i need it.

root.title("Dice!")
root.geometry("350x350") # temporary window size
root.mainloop() # this will be moved to the end of the program later.