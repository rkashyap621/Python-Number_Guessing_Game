# Python-Number_Guessing_Game

In this game, the computer will choose a number between 1 and 100, and you as the player has to guess the coreect number with available number of chances given to guess, to win the game.

# The Game Play Mechanism:
1. Computer will choose a random (or [pseudorandom](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)) number between 1 and 100.
2. The user will have two choice before guessing gameplay begins: EASY (Player will get 10 number of chances) and HARD (Player will get 5 number of number).
3. Now, the player will be prompted to guess the number.
4. If the guessed number is higher or lower than the number chosen by the computer, the user will be notified acoordingly. In these cases, since the guessed number are wrong the number of chances are penalized in every turn untill all the availables chances are exhausted.
5. Before the player exhausts all the available guesses, if the player can guess the number selected by computer, then the player wines. Otherwise, the player loses.
