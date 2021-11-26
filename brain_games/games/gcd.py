"""Return a conditions for the game "GCD'(greatest common divisor)."""

import random


def find_gcd(number1, number2):
    """Find a greatest common divisor (gcd).

    Args:
        number1: number for find GCD with number2
        number2: number for find GCD with number1

    Returns:
        return finded greatest common divisor.
    """
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    number_gcd = number2 + number1
    return number_gcd


def game_conditions():
    """
    Realize a game rules for the game 'greatest common divisor' (GCD).

    Returns:
        return 3 game's conditions:
        1. Rules of the game.
        2. String with 2 random numbers.
        3. Correct answer of the greatest common divisor (gcd) of 2 numbers.
    """
    game_rules = 'Find the greatest common divisor of given numbers.'
    round_count = 0
    question = ()
    correct_answer = ()
    while round_count < 3:
        first_rand_number = random.randint(1, 100) # noqa S311
        second_rand_number = random.randint(1, 100) # noqa S311
        string_question = (
            f'{first_rand_number} {second_rand_number}')
        question = (string_question, ) + question
        eval_answer = find_gcd(first_rand_number, second_rand_number)
        correct_answer = (eval_answer, ) + correct_answer
        round_count += 1
    return game_rules, question, correct_answer
