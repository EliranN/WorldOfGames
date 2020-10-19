import random
from time import sleep


def generate_sequence(difficulty_level):
    random_numbers_list = random.sample(range(1, 101), difficulty_level)
    return random_numbers_list


def get_list_from_user(difficulty_level):
    user_guessed_str = input("Enter " + str(difficulty_level) + " numbers please (separated by comma): ")
    user_guessed_list = user_guessed_str.split(",")
    user_guessed_list = [int(x) for x in user_guessed_list]
    return user_guessed_list


def is_list_equal(generated_list, user_guessed_list):
    # return generated_list == user_guessed_list
    generated_list.sort()
    user_guessed_list.sort()
    if generated_list == user_guessed_list:
        return True
    else:
        return False


def play(game_difficulty_level):
    generated_list = generate_sequence(game_difficulty_level)
    print(generated_list, end='')
    sleep(0.7)
    print(end="\r")
    user_guessed_list = get_list_from_user(game_difficulty_level)
    if is_list_equal(generated_list, user_guessed_list):
        print("You Won!")
    else:
        print("You Loss!")
