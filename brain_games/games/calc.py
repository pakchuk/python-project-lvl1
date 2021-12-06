"""Provide a dataset for the game "calculator'."""

import random

GAME_DESCRIPTION = 'What is the result of the expression?'
ROUNDS_COUNT = 3


def generate_question_answer():
    """Return question and answer for the game 'calculator'.

    Returns:
        question(str): expression of 2 random numbers and random math perator
        answer(str): calculation of expression from question
    """
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    math_operators = ('+', '-', '*')
    random_math_operator = random.choice(math_operators)
    question = (
        f'{random_number1} {random_math_operator} {random_number2}')
    answer = str(eval(question)) # noqa S307
    return question, answer
