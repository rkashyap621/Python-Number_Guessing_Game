import art

def display_art():
    print(art.logo)


def player_mode_selection():
    player_mode = input("Before you can guess the number. Select the game difficulty mode. Type 'Easy' for Easy Mode or Type 'Hard' for Hard Mode:\n").title()
    player_chance=0
    if player_mode == "Easy":
        player_chance = 10
        print("In", player_mode, "Mode you get", player_chance, "chances to guess the number.")
    else:
        player_chance = 5
        print("In", player_mode, "Mode you get", player_chance, "chances to guess the number.")
    return player_chance


def guess_check(num,check,lives,player_status):
    if check==num:
        print("Phew! You guessed the number. Congratulations! You win!")
        lives=0
        player_status=True
    else:
        if check>num:
            print("You guessed number is High.")
            lives-=1
            player_status = False
        else:
            print("You guessed number is Low.")
            lives-=1
            player_status = False
    return lives, player_status
