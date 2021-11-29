"""Realize engine for a control logic of the games."""

import brain_games.scripts.brain_games
import prompt


def logic(game_dataset):
    """
    Realize engine for a control logic of the games.

    Args:
        game_dataset:
            3 dataset for the game:
                1. Rules of the game.
                2. String with a math expression.
                3. Correct answer of the expression's calculation.

    Returns:
        return a message when user lose a game.
    """
    print('Welcome to the Brain Games!')
    brain_games.cli.welcome_user()
    game_rules = game_dataset[0]
    print(game_rules)
    correct_answer_count = 0
    while correct_answer_count < 3:
        question = (game_dataset[1][correct_answer_count])
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = game_dataset[2][correct_answer_count]
        uncorrect_answer_message = (
            "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
            "Let's try  again, {2}").format(
                answer, correct_answer, brain_games.cli.username)
        if correct_answer == answer:
            print('Correct!')
            correct_answer_count += 1
        else:
            return print(uncorrect_answer_message)
    print(f'Congratulations, {brain_games.cli.username}!')
