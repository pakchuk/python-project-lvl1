"""Provide a dataset for the game "prime'."""

import random

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    """Return boolean type for question 'is prime number'.

    Parameters:
        number(int): integer number

    Returns:
        boolean type about a is prime number or not
    """
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_question_answer():
    """Return question and answer for the game 'prime'.

    Returns:
        question(str): random number in range from 1 to 100
        answer(str): 'yes' - number is prime, 'no' - number is not prime.
    """
    number = random.randint(1, 100)
    question = str(number)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
