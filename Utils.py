import os

GAME_DIFFICULTY_LEVEL_RANGE = range(1, 6)
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


def get_input_and_check_if_valid(options, range_options, error_msg):
    while True:
        try:
            chosen_option = int(input(options))
            if chosen_option in range_options:
                return chosen_option
            else:
                raise ValueError
        except ValueError:
            print("\033[1m" + error_msg + "\033[0;0m")


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
