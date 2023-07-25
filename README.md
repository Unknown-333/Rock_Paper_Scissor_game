# **Rock, Paper, Scissors Game**
This is a simple Rock, Paper, Scissors game implemented in Python. The game is played between the user and the computer, and the first player to reach a score of 3 wins the game.

# **How to play**

1.Run the Python script to start the game.
2.The user will be prompted to pick their choice: Rock, Paper, or Scissors.
3.The computer will randomly select its choice.
4.The winner of each round will be determined based on the rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
5.The score of the user (player) and the computer will be displayed after each round.
6.The game will continue until either the user or the computer reaches a score of 3.
7.The game will announce the winner (either the user or the computer) and then terminate.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* The code begins with importing the random module, which is used to generate random choices for the computer in the Rock, Paper, Scissors game.

* The script defines three variables to keep track of the scores for the player, CPU (computer), and ties. It also creates a list possibleHands containing the three possible choices: "rock", "paper", and "scissor".

* Next, there is a function called checkForWinner, which takes two parameters: playerHand and computerHand. This function determines the winner of a round based on the game's rules and returns the result: "Player" if the player wins, "Cpu" if the computer wins, and "Tie" if it's a tie.

* The main game loop runs until either the player or the CPU reaches a score of 3. This is controlled by the while(playerScore != 3 and cpuScore != 3) loop.

* Inside the main loop, there is another loop that repeatedly asks the player to input their choice (rock, paper, or scissor). The input is converted to lowercase using playerHand = playerHand.lower() to handle different letter cases.

* The computer's choice is randomly selected using random.choice(possibleHands).

* After both the player and the computer have made their choices, the game's outcome is determined by calling the checkForWinner function with the player's and computer's choices as arguments. The result is then used to update the scores accordingly.

* After each round, the scores of the player, CPU, and ties are displayed using print(f"Your score : {playerScore} | CPU Score : {cpuScore} | Draw : {tieScore}").

* The game continues until either the player or the CPU reaches a score of 3. Once this condition is met, the game loop ends, and the winner (either the player or the CPU) is announced, followed by "Game over."
