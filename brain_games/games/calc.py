"""Prepair a dataset for the game "calculator'."""

import random

GAME_RULES = 'What is the result of the expression?'
ROUNDS_COUNT = 3

def gen(): 
    first_rand_number = random.randint(1, 10) # noqa S311
    second_rand_number = random.randint(1, 10) # noqa S311
    math_operation = ('+', '-', '*')
    random_math_operation = random.choice(math_operation) # noqa S311
    question = (
        f'{first_rand_number} {random_math_operation} {second_rand_number}')
    answer = str(eval(question)) # noqa S307
    return question, answer
