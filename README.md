# Rock-Paper-Scissors-Game

Author: Olubayode Ebenezer.

Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.

# A brief summary:

If the two players choose the same “character” it’s a tie, and the game repeats

Rock beats Scissors

Paper beats Rock

Scissors beats Paper

I created a simple version of this game with Python. In my version, one player is controlled by the computer and the other player controlled by myself - the user (i.e CPU vs Player). 

I made use of the inbuilt Python module random and its choice method.

Instructions:

I Created a new Python file and call it main.py. Inside it I created my game.
I Created a list to store all possible options:

"R" for "rock", 

"P" for "paper", 

"S" for "scissors".

When the program is run, I asked the user to pick an option between "R", "P" or "S"
If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
I Used the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
I Checked both player's moves: 
If there is a winner, print the winner, and the program ends. 
If it's a tie (the computer and player pick the same move), restart the game from step 3
Resources:

How to Play Rock, Paper, Scissors (https://www.youtube.com/watch?v=ND4fd6yScBM)

Rock paper scissors - Wikipedia (https://en.wikipedia.org/wiki/Rock_paper_scissors)

Introduction to Python Modules (https://www.youtube.com/watch?v=uoVUOTPL9Rw&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=26)

Python Random Module (https://www.w3schools.com/python/module_random.asp)

Python random choice() function to select a random item from a List and Set (https://pynative.com/python-random-choice/)

For Loops (https://www.youtube.com/watch?v=P9sIg93Boso&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=18)

While Loops (https://www.youtube.com/watch?v=J8dkgM8Mck0&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=19)
