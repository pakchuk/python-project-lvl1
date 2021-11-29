"""Prepair a dataset for the game "prime'."""

import random


def is_prime():
    """
    Check is number a prime number.

    Returns:
        return:
            str(number): random number (str type) in range from 1 to 100
            answer: 'yes' - number is prime, 'no' - number is not prime.
    """
    number = random.randint(1, 100) # noqa S311
    for i in range(2, number):
        if number == 1 or number % i == 0:
            answer = 'no'
            break
        else:
            answer = 'yes'
    return str(number), answer


def make_game_dataset():
    """
    Make  a dataset of the game 'prime' for engine.py.

    Returns:
        return dataset for 3 rounds of the game:
        1. Rules of the game.
        2. String with random number in range from 1 to 100.
        3. Correct answer: 'yes' - number is prime,
        'no - number is not a prime'.
    """
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = ()
    correct_answer = ()
    round_count = 0
    while round_count < 3:
        number, answer = is_prime()
        question = question + (number, )
        correct_answer = correct_answer + (answer, )
        round_count += 1
    return game_rules, question, correct_answer
