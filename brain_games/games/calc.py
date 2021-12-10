"""Provide a dataset for the game "calculator'."""

import operator
import random

GAME_DESCRIPTION = 'What is the result of the expression?'


def calc(num1, num2, operation):
    """Return a result of math expression.

    Parameters:
        num1(int): first number for math expression
        num2(int): second number for math expression
        operation(function): one of standart operator from (+,-,*)

    Returns:
        the result(int) of evaluating an expression of two numbers (num1, num2)
    """
    operation_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    return(operation_dict[operation](num1, num2))


def generate_question_answer():
    """Return question and answer for the game 'calculator'.

    Returns:
        question(str): expression of 2 random numbers and random math perator
        answer(str): calculation of expression from question
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(('+', '-', '*'))
    question = f'{num1} {operation} {num2}'
    answer = str(calc(num1, num2, operation))
    return question, answer
