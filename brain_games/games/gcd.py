"""Provide a dataset for the game "GCD'(greatest common divisor)."""

import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
ROUNDS_COUNT = 3


def generate_question_answer():
    """Return question and answer for the game 'GCD'.

    Returns:
        question(str): 2 random numbers
        answer(str): GCD of 2 numbers from question
    """
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question = f'{random_number1} {random_number2}'
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 = random_number1 % random_number2
        else:
            random_number2 = random_number2 % random_number1
    gcd = random_number2 + random_number1
    answer = str(gcd)
    return question, answer
