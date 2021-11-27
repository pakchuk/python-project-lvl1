"""Prepair a dataset for the game "progression'."""

import random


def make_progression():
    """
    Make a arithmetic progression.

    Arithmetic progression with random quantity elements in range
    from 5 to 10 and random start number in range from 1 to 99.

     Returns:
        return: atithmetic progression.
    """
    start_number = random.randint(1, 99) # noqa S311
    length_progress = random.randint(5, 10) # noqa S311
    diff_progress = random.randint(1, 9) # noqa S311
    progression = ()
    while length_progress > 0:
        progression = progression + (start_number, )
        start_number = start_number + diff_progress
        length_progress -= 1
    return progression


def make_game_dataset():
    """
    Make  a dataset of the game 'progression' for engine.py.

    Returns:
        return dataset:
        1. Rules of the game.
        2. String with arithmetic progression where one of numbers is hidden.
        3. Correct answer - number of a hidden element.
    """
    game_rules = 'What number is missing in the progression?'
    correct_answer = ()
    question = ()
    round_count = 0
    while round_count < 3:
        progression = make_progression()
        finish_range = len(progression) - 1
        position_hidden_number = random.randint(0, finish_range) # noqa S311
        hidden_number = progression[position_hidden_number]
        correct_answer = correct_answer + (hidden_number, )
        cut1 = progression[:position_hidden_number]
        cut2 = progression[position_hidden_number + 1:]
        progression_hidden = cut1 + ('..', ) + cut2
        string_progressinon_hidden = ''
        for i in range(0, len(progression)):
            string_progressinon_hidden = (
                string_progressinon_hidden + str(progression_hidden[i]) + ' ')
        question = question + (string_progressinon_hidden[:-1], )
        round_count += 1
    return game_rules, question, correct_answer
