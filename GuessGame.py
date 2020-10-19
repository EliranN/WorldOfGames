from random import randint

import Utils


def generate_number(difficulty_level):
    secret_number = randint(1, difficulty_level)
    return secret_number


def get_guess_from_user():
    ask_for_guess_number_input = "Enter your guess number please: "
    guess_number_error_msg = "Guess number should be a number between 1 to 5\n"
    chosen_option = Utils.get_input_and_check_if_valid(ask_for_guess_number_input, Utils.GAME_DIFFICULTY_LEVEL_RANGE,
                                                       guess_number_error_msg)
    return chosen_option


def compare_results(secret_number, user_guessed_number):
    if secret_number == user_guessed_number:
        return True
    else:
        return False


def play(game_difficulty_level):
    difficulty_level = game_difficulty_level
    generate_number(difficulty_level)
    secret_number = generate_number(difficulty_level)
    user_guessed_number = get_guess_from_user()
    if compare_results(secret_number, user_guessed_number):
        print("You Won!")
    else:
        print("You Loss!")
