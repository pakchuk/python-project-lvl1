"""Realize engine for a control logic of the games."""

import brain_games.scripts.brain_games
import prompt


def logic(game_dataset):
    """
    Realize engine for a control logic of the games.

    Args:
        game_dataset:
            3 dataset (for 3 rounds) for the game:
                1. Rules of the game.
                2. String with a math expression.
                3. Correct answer of the expression's calculation.
    """
    print('Welcome to the Brain Games!')
    brain_games.cli.welcome_user()
    game_rules = game_dataset[0]
    print(game_rules)
    correct_answer_count = 3
    for i in range(0, correct_answer_count):
        question = (game_dataset[1][i])
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = game_dataset[2][i]
        game_win_message = (f'Congratulations, {brain_games.cli.username}!')
        game_over_message = (
            "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
            "Let's try  again, {2}").format(
                answer, correct_answer, brain_games.cli.username)
        if correct_answer != answer:
            game_result = game_over_message
            break
        print('Correct!')
        game_result = game_win_message
    print(game_result)
