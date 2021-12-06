"""Provide a dataset for the game "progression'."""

import random

GAME_DESCRIPTION = 'What number is missing in the progression?'
ROUNDS_COUNT = 3


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
    # create progression (tuple):
    first_numb_progression = random.randint(1, 99)
    length_progression = random.randint(5, 10)
    diff_progression = random.randint(1, 9)
    progression = ()
    i = length_progression
    while i > 0:
        progression = progression + (first_numb_progression, )
        first_numb_progression = first_numb_progression + diff_progression
        i -= 1
    # create progression with hidden number (str):
    final_possible_index_hidden_numb = len(progression) - 1
    index_hidden_number = random.randint(0, final_possible_index_hidden_numb)
    progression_before_hide_numb = progression[:index_hidden_number]
    progression_after_hide_numb = progression[index_hidden_number + 1:]
    progression_with_hidden_number = (
        progression_before_hide_numb + ('..', ) + progression_after_hide_numb)
    question = ''
    # transform progression with hidden number from tuple to str:
    for i in progression_with_hidden_number:
        question = question + str(i) + ' '
    question = question[:-1]
    answer = str(progression[index_hidden_number])
    return question, answer
