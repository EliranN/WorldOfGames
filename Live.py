import Score
import Utils
from CurrencyRouletteGame import play as play_currency_game
from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game


def welcome(name):
    return "Hello %s and welcome to the World of Games (WoG).\nHere you can find many cool games to play." % name


def load_game():
    game_to_play = "Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and " \
                   "you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n" \
                   "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    game_to_play_range = range(1, 4)
    game_to_play_error_msg = "Game to play should be a number between 1 to 3\n"
    difficulty_level = "Please choose game difficulty from 1 to 5: "
    game_difficulty_level_error_msg = "Difficulty level should be a number between 1 to 5\n"
    chosen_game = Utils.get_input_and_check_if_valid(game_to_play, game_to_play_range, game_to_play_error_msg)
    difficulty_level = Utils.get_input_and_check_if_valid(difficulty_level,
                                                          Utils.GAME_DIFFICULTY_LEVEL_RANGE,
                                                          game_difficulty_level_error_msg)
    if chosen_game == 1:
        play_memory_game(difficulty_level)
        Score.add_score(difficulty_level)
    elif chosen_game == 2:
        play_guess_game(difficulty_level)
        Score.add_score(difficulty_level)
    elif chosen_game == 3:
        play_currency_game(difficulty_level)
        Score.add_score(difficulty_level)
