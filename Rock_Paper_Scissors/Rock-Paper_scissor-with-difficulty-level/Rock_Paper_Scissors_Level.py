import random

cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["rock", "paper", "scissor"]

difficulty_levels = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

def checkForWinner(playerHand, computerHand):
    if (playerHand == "rock" and computerHand == "paper"):
        print("You Lose!")
        return "Cpu"
    elif(playerHand == "rock" and computerHand == "scissor"):
        print("You Win!")
        return "Player"
    elif(playerHand == "scissor" and computerHand == "paper"):
        print("You Win!")
        return "Player"
    elif(playerHand == "scissor" and computerHand == "rock"):
        print("You Lose!")
        return "Cpu"
    elif(playerHand == "paper" and computerHand == "rock"):
        print("You Win!")
        return "Player"
    elif(playerHand == "paper" and computerHand == "scissor"):
        print("You Lose!")
        return "Cpu"
    else:
        print("It's a tie!")
        return "Tie"

# Function to get the computer's choice based on the difficulty level and player's previous choice
def getComputerChoice(difficulty, playerHand):
    if difficulty == 1:  # Easy: Computer chooses randomly
        return random.choice(possibleHands)
    elif difficulty == 2:  # Medium: Computer chooses randomly, but with higher chance of choosing winning hand
        winning_hand = {"rock": "paper", "paper": "scissor", "scissor": "rock"}
        return winning_hand[random.choice(possibleHands)]
    elif difficulty == 3:  # Hard: Computer chooses the hand that wins against the player's previous choice
        winning_hand = {"rock": "paper", "paper": "scissor", "scissor": "rock"}
        return winning_hand[playerHand]

while True:
    difficulty_choice = input("Choose the difficulty level (easy, medium, hard): ")
    difficulty_choice = difficulty_choice.lower()
    if difficulty_choice in difficulty_levels:
        difficulty = difficulty_levels[difficulty_choice]
        break
    else:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")

while playerScore != 3 and cpuScore != 3:
    while True:
        playerHand = input("\nPick your choice, Rock, Paper, or Scissor: ")
        playerHand = playerHand.lower()
        if playerHand in possibleHands:
            break
        else:
            print("Invalid input. Please give correct input: Rock, Paper, or Scissor")

    computerHand = getComputerChoice(difficulty, playerHand)

    print(f"\nYou picked : {playerHand}")
    print(f"Computer picked : {computerHand}")
    result = checkForWinner(playerHand, computerHand)
    if result == "Player":
        playerScore += 1
    elif result == "Cpu":
        cpuScore += 1
    else:
        tieScore += 1
    print(f"\nYour score: {playerScore} | CPU Score: {cpuScore} | Draws: {tieScore}")

print("\nGame over")

if playerScore == 3:
    print("Congratulations! You won the game!")
elif cpuScore == 3:
    print("Oops! You lost the game. Better luck next time!")
