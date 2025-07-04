def number_guess_game ():
    user_range = [1, 100]

    stages = choose_level()

    user_number = int(input("Pick a random number from 1 to 100: \n"))

    print(f"I can pick your number in {stages} stages")
    print(f"If I do not find your number in {stages} stages, you win")
    print("But you should be honest with me")

    while True:
        is_user_honest = input("Will you? y/n \n")
        if is_user_honest == 'y':
            break
        elif is_user_honest == 'n':
            not_honest_end()
            return
        else:
            not_decode_user_input()

    while True:
        is_user_ready = input("Are you ready? y/n \n")
        if is_user_ready == 'y':
            break
        elif is_user_ready == 'n':
            not_ready_end()
            return
        else:
            not_decode_user_input()

    while stages > 0:
        guess_number = (user_range[0] + user_range[1]) // 2
        is_guessed_num = input(f"Is your number {guess_number}? y/n \n")
        if is_guessed_num == 'y':
            if guess_number != user_number:
                misclick_end(user_number, guess_number)
                return
            computer_win_end()
            return
        else:
            if guess_number == user_number:
                sweet_lie_end()
                return
            stages -= 1
            if stages == 0:
                user_win_end()
            else:
                print("Oh I was wrong... Help me")
        user_choice = input(f"Is it bigger than {guess_number} ? y/n \n")
        if user_choice == 'y':
            user_range[0] = guess_number + 1
        else:
            user_range[1] = guess_number - 1
        print("~" * 25)

def choose_level():
    game_modes = {
        "easy": 5,
        "mid": 6,
        "hard": 7
    }
    level = None
    stages = None

    while level not in game_modes:
        level = input("Choose level to continue: easy, mid, hard\n")
        if level in game_modes:
            stages = game_modes[level]
        else:
            print("I said choose the level")
            print("Please")
    return stages

def not_decode_user_input():
    print("I do not understand your cribbles-scribbles")
    print("Try one more time")

def print_end():
    print("The end")
    print("~~~~~~~~~~~~~")
    print("\n" * 24)
    print("Hey...")
    print("But...")
    print("What about...")
    print("I just have a thought")

    while True:
        is_start_again = input("if you want to start again... y/n\n")
        if is_start_again == 'y':
            print('Thank you!')
            print('I always liked you')
            print('Prepare to lose!')
            number_guess_game()
            return
        elif is_start_again == 'n':
            print("I understand you")
            print("I misbehaved")
            print("But it was fun for me")
            print("Was it fun for you?")
            print("Oh certainly it was")
            print("Please come back soon...")
            print("I will always be remembering you. Even if... you forget")
            return
        else:
            print("I do not understand your cribbles-scribbles")
            print("Try one more time")

def user_win_end():
    print("You defeated me. Very wise man indeed")
    print_end()

def computer_win_end():
    print("Oh, I knew it! Computer ALWAYS wins")
    print_end()

def not_honest_end():
    print("NONONO I cannot play with liars")
    print_end()

def not_ready_end():
    print("If you are not ready, then I must go elsewhere")
    print_end()

def misclick_end(user_number, guess_number):
    print("You misclicked")
    print("That was not YOUR NUMBER")
    print(f"You picked {user_number}")
    print(f"And I said {guess_number} which is not {user_number}")
    print("Are you trolling me? 😒")
    print_end()

def sweet_lie_end():
    print("You S*CKER lied to ME!!!")
    print("~~~TEAM COMPUTER~~~")
    print("COMPUTER")
    print("ALWAYS")
    print("WINS")
    print("!!!")
    print_end()


print("Welcome to Powerful Djinni")
print("I can guess all your thoughts")
print("Well... all thought connected to numbers")
number_guess_game()