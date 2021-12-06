"""Provide a dataset for the game "prime'."""

import random

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".')
ROUNDS_COUNT = 3


def generate_question_answer():
    """Return question and answer for the game 'prime'.

    Returns:
        question(str): random number in range from 1 to 100
        answer(str): 'yes' - number is prime, 'no' - number is not prime.
    """
    random_number = random.randint(1, 100)
    question = str(random_number)
    for i in range(2, random_number):
        if random_number == 1:
            answer = 'no'
        elif random_number % i == 0:
            answer = 'no'
            break
        else:
            answer = 'yes'
    return question, answer
