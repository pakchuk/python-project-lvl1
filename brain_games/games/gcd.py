"""Provide a dataset for the game "GCD'(greatest common divisor)."""

import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    """Return GCD of 2 numbers.

    Parameters:
        num1(int): integer number
        num2(int): integer number

    Returns:
        GCD(int) of num1, num2
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def generate_question_answer():
    """Return question and answer for the game 'GCD'.

    Returns:
        question(str): 2 random numbers
        answer(str): GCD of 2 numbers from question
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    answer = str(find_gcd(num1, num2))
    return question, answer
