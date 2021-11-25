"""Return a condition for the game "calculator'."""

import random


def calc():
    """
    Realize a conditions for the game 'calculator'.

    Returns:
        return 3 game's conditions:
        1. Rules of the game.2.
        2. String with a math expression.
        3. Correct answer of the expression's calculation.
    """
    game_rules = 'What is the result of the expression?'
    round_count = 0
    question = ()
    correct_answer = ()
    while round_count < 3:
        first_rand_number = random.randint(1, 10) # noqa S311
        second_rand_number = random.randint(1, 10) # noqa S311
        math_operation = ('+', '-', '*')
        random_math_operation = random.choice(math_operation) # noqa S311
        string_question = (
            f'{first_rand_number} {random_math_operation} {second_rand_number}')
        eval_answer = eval(string_question) # noqa S307
        question = (string_question, ) + question
        correct_answer = (eval_answer, ) + correct_answer
        round_count += 1
    return game_rules, question, correct_answer
