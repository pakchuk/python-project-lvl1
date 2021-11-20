"""Script with greetings to user and asking username."""
#!/usr/bin/env python3 # noqa:E265

import brain_games.cli


def main():
    """Greetings for user, ask username."""
    print('Welcome to the Brain Games!')
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
