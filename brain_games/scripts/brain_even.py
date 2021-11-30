"""Script with a game "check number for an even"."""
#!/usr/bin/env python3 # noqa:E265

import random

import brain_games.scripts.brain_games
import prompt


def is_even():
    """
    Ask user about an even of a number.

    Returns:
        return uncorrect answer message
    """
    print('Welcome to the Brain Games!')
    brain_games.cli.welcome_user()
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(game_rules)
    correct_answer_count = 0
    while correct_answer_count < 3:
        number = random.randint(1, 100) # noqa S311
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        uncorrect_answer_message = (
            "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
            "Let's try again, {2}!").format(
                answer, correct_answer, brain_games.cli.username)
        if correct_answer == answer:
            print('Correct!')
            correct_answer_count += 1
        else:
            return print(uncorrect_answer_message)
    print(f'Congratulations, {brain_games.cli.username}!')


def main():
    """Start function is_even()."""
    is_even()


if __name__ == '__main__':
    main()
