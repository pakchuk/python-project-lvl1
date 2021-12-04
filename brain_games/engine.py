import prompt


def control_game(game_dataset):
    print('Welcome to the Brain Games!')
    player_name = prompt.string("May I Have Your Name: ")
    print('Hello,' +  player_name)
    game_rules = game_dataset.GAME_RULES
    print(game_rules)
    index = 0
    while index < game_dataset.ROUNDS_COUNT:
        question, answer = game_dataset.gen()
        print('COMING: ' + answer )
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
        index += 1
        game_result = game_win_message
    print(game_result)
