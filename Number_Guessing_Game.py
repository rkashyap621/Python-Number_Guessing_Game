import random
import Game_Manager as game

number= random.randint(1,100)
player_lives= 0
game_won= False
game_started = False
print("Welcome to Number Guessing Game.")
game_start=input("Would you like to start the game? (y/n):\n").lower()
if game_start=="n":
    print("Thank you for using Number Guessing Game.")
else:
    game_started = True
    game.display_art()
    print("I am thinking of a number between 1 and 100.")
    player_lives=game.player_mode_selection()

while player_lives>0:
    print("\nGet Ready! You have", player_lives, "chances left to guess the number.")
    guess=int(input("Guess the number:"))
    [player_lives, game_won]=game.guess_check(number,guess,player_lives,game_won)

if not game_won and game_started:
    print("Psst! You have no chances left!")
    reveal=input("Would you like to reveal the number? (y/n):\n").lower()
    if reveal=="y":
        print("The number you had to guess was "+str(number)+".")
    print("Better Luck Next Time!")
