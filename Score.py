from decimal import Decimal

from Utils import SCORES_FILE_NAME


def add_score(difficulty_level):
    points_of_winning = (difficulty_level * 3) + 5
    try:
        score_file = open(SCORES_FILE_NAME, 'r')
        score_file.close()
    except FileNotFoundError:
        init_score_file()
    with open(SCORES_FILE_NAME, 'a+') as score_file:
        score_file.write(',' + str(points_of_winning))
    with open(SCORES_FILE_NAME, 'r') as score_file:
        for tav in score_file:
            score_list = tav.split(',')
        sum(Decimal(i) for i in score_list)


def init_score_file():
    init_file = open(SCORES_FILE_NAME, 'a+')
    init_file.write('0')
    init_file.close()
