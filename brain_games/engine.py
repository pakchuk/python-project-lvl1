"""Module for contol a logic of the game."""

import prompt

ROUNDS_COUNT = 3


def run_game(game):
    """
    Control a logic of the CLI game.

    Game logic step by step: greet player, ask player name,
    show a game description, show a question, recieve player's
    answer, check player's answer, inform user about correction of
    plaeyr's answer. 3 correct answer in a row - win the game,
    first wrong answer - game over.

    Parameters:
        game(module): module which provide a dataset of the game:
            - game description;
            - function, which returns question and answer.
    """
    print('Welcome to the Brain Games!')
    game_description = game.GAME_DESCRIPTION
    username = prompt.string('May I Have Your Name? ')
    print(f'Hello, {username}!\n{game_description}')
    for _i in range(0, ROUNDS_COUNT):
        question, answer = game.generate_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(
                ("'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
                 "Let's try again, {2}!").format(user_answer, answer, username))
            game_win = False
            break
        else:
            print('Correct!')
            game_win = True
    if game_win:
        print(f'Congratulations, {username}!')
