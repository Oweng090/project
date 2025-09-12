"""
  Name: GIU_Dice_Roller
  Created by: Owen Graham
  Created: 
  Purpose: Roll a dice as its own little Gui window
"""

# import tkinter for the Gui
import tkinter as tk
import random


#Create the individual window.
root = tk.Tk()

# making labels.
label = tk.Label(root, text="Dice Roll!", font=("Arial", 14)) # label for the first dice roll ( will be made into an image of a dice. )
label.pack(pady=20)

label2 = tk.Label(root, text="", font=("Arial", 14)) # label for the second dice result ( this label will be made into an image.)
label2.pack(pady=20)

total_label = tk.Label(root, text="", font=("Arial", 14)) # label for the total of the rolls.
total_label.pack(pady=20)

roll_Button = tk.Button(root, text="Roll Dice", width=20, command=lambda: roll_dice1("Roll!")) # defining a button for the GUI
roll_Button.place(x=100, y=200) # making it so the program displays the button where i need it.

root.title("Dice!")
root.geometry("350x350") # temporary window size

# create a function for the dice rolling
def roll_dice1(side):
    sides = [1, 2, 3, 4, 5, 6]
    side = random.choice(sides) 

    if (side == 1):
        # the side will be 1
        label.config(text="First dice rolled: 1") # Changing the label to show what you rolled ( this is a place holder for the images in the future.)
    elif(side == 2):
        # the side will be 2
        label.config(text="First dice rolled: 2") # Changing the label to show what you rolled ( this is a place holder for the images in the future.)
    elif(side == 3):
        # the side will be 3
        label.config(text="First dice rolled: 3") # Changing the label to show what you rolled ( this is a place holder for the images in the future.)
    elif(side == 4):
        #the side will be 4
        label.config(text="First dice rolled: 4") # Changing the label to show what you rolled ( this is a place holder for the images in the future.)
    elif(side == 5):
        # the side will be 5
        label.config(text="First dice rolled: 5") # Changing the label to show what you rolled ( this is a place holder for the images in the future.)
    else:
        # the side will be 6
        label.config(text="First dice rolled: 6") # Changing the label to show what you rolled ( this is a place holder for the images in the future.)

    sides2 = [1, 2, 3, 4, 5, 6]
    side2 = random.choice(sides2)

    if(side2 == 1):
        label2.config(text="Second dice rolled: 1") # these labels will show the result of the second dice.
    elif(side2 == 2):
        label2.config(text="Second dice rolled: 2") # the labels will be swapped out for images in the future
    elif(side2 == 3):
        label2.config(text="Second dice rolled: 3")
    elif(side2 == 4):
        label2.config(text="Second dice rolled: 4")
    elif(side2 == 5):
        label2.config(text="Second dice rolled: 5")
    else:
        label2.config(text="Second dice rolled: 6")
        
    total_roll = side + side2
    total_label.config(text=f"Total roll: {total_roll}")

root.mainloop() # this will be moved to the end of the program later.