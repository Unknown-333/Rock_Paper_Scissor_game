import random
import tkinter

root = tkinter.Tk()
root.geometry("400x400")
root.title("Rock-Paper-Scissors Game")

# Computer Value
computer_dict = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
}

# Global variable to store the player's choice
player_choice = None

# Global variable to store the difficulty level
difficulty = None

# Function to set the player's choice and start the game
def set_player_choice(choice):
    global player_choice
    player_choice = choice
    play_game()

# If player selects rock
def player_rock():
    set_player_choice("rock")

# If player selects paper
def player_paper():
    set_player_choice("paper")

# If player selects scissors
def player_scissors():
    set_player_choice("scissors")

# Function to check for the winner
def checkForWinner(playerHand, computerHand):
    playerHand = playerHand.lower()
    computerHand = computerHand.lower()

    if (playerHand == "rock" and computerHand == "paper") or \
       (playerHand == "paper" and computerHand == "scissors") or \
       (playerHand == "scissors" and computerHand == "rock"):
        return "Computer Wins"
    elif (playerHand == "rock" and computerHand == "scissors") or \
         (playerHand == "paper" and computerHand == "rock") or \
         (playerHand == "scissors" and computerHand == "paper"):
        return "You Win"
    else:
        return "Tie"

# Function to get the computer's choice based on the difficulty level and player's previous choice
def getComputerChoice(difficulty, player_choice):
    if difficulty == "easy":  # Easy: Computer chooses randomly
        return random.choice(list(computer_dict.values()))
    elif difficulty == "medium":  # Medium: Computer chooses randomly, but with higher chance of winning hand
        winning_hand = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
        return winning_hand[random.choice(list(computer_dict.values()))]
    elif difficulty == "hard":  # Hard: Computer chooses the hand that wins against the player's previous choice
        if player_choice == "rock":
            return "Paper"
        elif player_choice == "paper":
            return "Scissors"
        elif player_choice == "scissors":
            return "Rock"

# Function to display the result on the GUI
def display_result(player_choice, computer_choice, result):
    l4.config(text=result)
    l1.config(text=player_choice)
    l3.config(text=computer_choice)

# Function to play the game
def play_game():
    global difficulty
    global player_choice

    if difficulty is not None and player_choice is not None:
        computer_choice = getComputerChoice(difficulty, player_choice)
        result = checkForWinner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result)

# Function to reset the game
def reset_game():
    global player_choice
    player_choice = None
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player         ")
    l3.config(text="Computer")
    l4.config(text="")

# Add Labels, Frames and Buttons
tkinter.Label(root,
              text='Choose the difficulty level (select the difficulty first): ',
              font=("monoid", 12),
              fg="blue").pack(pady=20)

# Buttons for difficulty levels
tkinter.Button(root, text="Easy",
               font=("monoid", 10),
               fg="black", bg="light grey", command=lambda: set_difficulty("easy")).pack(pady=5)
tkinter.Button(root, text="Medium",
               font=("monoid", 10),
               fg="black", bg="light grey", command=lambda: set_difficulty("medium")).pack(pady=5)
tkinter.Button(root, text="Hard",
               font=("monoid", 10),
               fg="black", bg="light grey", command=lambda: set_difficulty("hard")).pack(pady=5)

frame = tkinter.Frame(root)
frame.pack()

l1 = tkinter.Label(frame,
                   text="Player         ",
                   font=("monoid", 10))

l2 = tkinter.Label(frame,
                   text="VS         ",
                   font=("monoid", 12))

l3 = tkinter.Label(frame, text="Computer", font=("monoid", 10))

l1.pack(side='left')
l2.pack(side='left')
l3.pack()

l4 = tkinter.Label(root,
                   text="",
                   font=("monoid", 12),
                   bg="white",
                   width=15,
                   borderwidth=2,
                   relief="solid")
l4.pack(pady=20)

frame1 = tkinter.Frame(root)
frame1.pack()

b1 = tkinter.Button(frame1, text="Rock",
                    font=("monoid", 12),
                    width=7, bg="light blue",
                    command=player_rock)

b2 = tkinter.Button(frame1, text="Paper ",
                    font=("monoid", 12),
                    width=7, bg="light blue",
                    command=player_paper)

b3 = tkinter.Button(frame1, text="Scissors",
                    font=("monoid", 12),
                    width=7, bg="light blue",
                    command=player_scissors)

b1.pack(side='left', padx=10)
b2.pack(side='left', padx=10)
b3.pack(padx=10)

tkinter.Button(root, text="Reset Game",
               font=("monoid", 12),
               fg="red",
               bg="light grey", command=reset_game).pack(pady=20)

# Function to set the difficulty level and start the game
def set_difficulty(diff):
    global difficulty
    difficulty = diff
    play_game()

# Execute Tkinter
root.mainloop()
