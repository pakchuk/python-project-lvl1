"""Module ask name of player."""

import prompt


def welcome_user():
    """Ask name of user and return name of user."""
    username_question = 'May I have your name? '
    global username
    username = prompt.string(username_question)
    print('Hello, {0}!'.format(username))


def main():
    """Start a welcome_user function."""
    welcome_user()


if __name__ == '__main__':
    main()
