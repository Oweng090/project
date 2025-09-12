"""
    Filename: Rock_Paper_Scissors.py
    Author: Owen Graham
    Created: 8/29/25
    Purpose: play rock paper scissors with the computer
"""
# TODO make the tools i need to make this program
import random
import tkinter as tk # I asked the AI what I could use to make a gui version of rock paper scissors
# TODO make a window for the program
root = tk.Tk() # Starting the tkinter and creating the main gui window
root.title("Rock_Paper_Scissors")#
root.geometry("300x350")#
# TODO make labels to interact with user
# Asked AI how to make a tkinter label then made labels for the program
label = tk.Label(root, text="Make your move", font=("Arial", 14)) # making the first label to tell the user to start
label.pack(pady=20)

Comlabel = tk.Label(root, text=" ", font=("Arial", 14)) # Making a label with no teext for future use.
Comlabel.pack(pady=20)

ResultLabel = tk.Label(root, text=" ", font=("Arial", 14)) # Again, making a lable for future use 
ResultLabel.pack(pady=20)
# TODO make a list of choices the player and computer can make.
choices = ["Rock", "Paper", "Scissors"]
# TODO make a function to determine if you win lose or tie
def play(playerChoice):
    computerChoice = random.choice(choices)

    label.config(text=f"You chose {playerChoice}") # Reconfiguring the first label to show what the user chose
    Comlabel.config(text=f"Computer Chose {computerChoice}") # Configuring the first blank label to show what the computer chose

    if playerChoice == computerChoice: # if the user and computer input are the same its a tie
        result = "Its a tie."
    elif (playerChoice == "Rock" and computerChoice == "Scissors") or \
         (playerChoice == "Paper" and computerChoice == "Rock") or \
        (playerChoice == "Scissors" and computerChoice == "Paper"):
        result = "You win" # Making it so if the user input beats the computer input the result will be you win.
    else:
        result = "You lose" # anythin else the computer will win

    ResultLabel.config(text=result) # Configuring the result label to show if you won lost or tied.
# TODO make buttons the user can click to make their choice.
# Asked AI how to make a button and I created buttons based on what it gave me
RockButton = tk.Button(root, text="Rock", width=20, command=lambda: play("Rock")) # the Button for the user input "Rock"
PaperButton = tk.Button(root, text="Paper", width=20, command=lambda: play("Paper")) # the button for the user input "Paper"
ScissorsButton = tk.Button(root, text="Scisors", width=20, command=lambda: play("Scissors")) # the button for the user input "Scissors"

RockButton.pack() #
PaperButton.pack() # Displaying the buttons in the rock paper scissors order.
ScissorsButton.pack() #

# TODO make the main GUI (Graphical user interface) 
root.mainloop()