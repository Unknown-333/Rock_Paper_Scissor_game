import random

cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["rock", "paper", "scissor"]


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
    
while(playerScore != 3 and cpuScore != 3):
    while True:
        playerHand = input("\n Pick your choice, Rock, Paper, or Scissor: ")
        playerHand = playerHand.lower()
        if(playerHand == "rock" or playerHand == "paper" or playerHand == "scissor"):
            break
        else:
            print("Invalid input. Please give correct input :")

    computerHand = random.choice(possibleHands)

    print(f"You picked : {playerHand}")
    print(f"Computer picked : {computerHand}")
    result = checkForWinner(playerHand, computerHand)
    if(result == "Player"):
        playerScore += 1
    elif(result == "Cpu"):
        cpuScore += 1
    print(f"Your score : {playerScore} | CPU Score : {cpuScore} | Draw : {tieScore}")

print("Game over")




