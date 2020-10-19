from random import randint

from currency_converter import CurrencyConverter


def get_money_interval(difficulty_level):
    random_usd_amount = randint(1, 100)
    currency_converter = CurrencyConverter()
    t = currency_converter.convert(random_usd_amount, 'USD', 'ILS')
    d = difficulty_level
    generated_interval = t - (5 - d), t + (5 - d)
    return random_usd_amount, generated_interval


def get_guess_from_user(random_usd_amount):
    user_guessed_value = input("Enter your ILS guess value for %d USD please: " % random_usd_amount)
    return user_guessed_value


def play(game_difficulty_level):
    difficulty_level = game_difficulty_level
    random_usd_amount, generated_interval = get_money_interval(difficulty_level)
    user_guessed_value = get_guess_from_user(random_usd_amount)
    if generated_interval[0] <= float(user_guessed_value) <= generated_interval[1]:
        print("You Won!")
        return True
    else:
        print("You Loss!")
        return False
