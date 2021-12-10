"""Provide a dataset for the game "progression'."""

import random

GAME_DESCRIPTION = 'What number is missing in the progression?'


def make_progression(first_num, diff, length):
    """Return arithmetic progression.

    Parameters:
        first_num(int): first mumber of progression
        diff(int): differense of the progression
        length(int): quantity on numbers of progression

    Returns:
        progression(list): arithmetic progression, every element is str type
    """
    progression = []
    for _i in range(length):
        progression.append(str(first_num))
        first_num += diff
    return progression


def generate_question_answer():
    """Return question and answer for the game 'progression'.

    Function generate an arithmetic progression with random length
    in range from 5 to 10 numbers, random first number in range from 1 to 100,
    and random differense of progression. Question for player is a generated
    progression with one hidden number.

    Returns:
        question(str): arithmetic progression with one hidden number
        answer(str): hidden number of progression from question
    """
    # create progression (list with str type numbers):
    first_num = random.randint(1, 99)
    length = random.randint(5, 10)
    diff = random.randint(1, 9)
    progression = make_progression(first_num, diff, length)
    # create progression with hidden number (str):
    hidden_index = random.randint(0, len(progression) - 1)
    answer = progression.pop(hidden_index)
    progression.insert(hidden_index, '..')
    question = ' '.join(progression)
    return question, answer
