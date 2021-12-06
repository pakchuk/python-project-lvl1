"""Module for contol a logic of the game."""

import prompt


def control_game(game_dataset):
    """
    Control a logic of the CLI game.

    Game logic step by step: greet plyer, ask player name,
    show a game description, show a question, recieve player's
    answer, 3 correct answer in a row - win the game, first
    wrong answer - game over.

    Parameters:
        game_dataset(module): module which provide a dataset of the game:
            - game description;
            - count of rounds;
            - function, which returns question and answer.
    """
    greeting = 'Welcome to the Brain Games!'
    print(greeting)
    game_description = game_dataset.GAME_DESCRIPTION
    player_name = prompt.string('May I Have Your Name? ')
    print(f'Hello, {player_name}!\n{game_description}')
    rounds_count = game_dataset.ROUNDS_COUNT
    i = 0
    while i < rounds_count:
        question, answer = game_dataset.generate_question_answer()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        game_win_message = (f'Congratulations, {player_name}!')
        game_over_message = (
            "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
            "Let's try again, {2}!").format(
                player_answer, answer, player_name)
        if player_answer != answer:
            game_result = game_over_message
            break
        print('Correct!')
        i += 1
        game_result = game_win_message
    print(game_result)
