"""Script for start a game 'Progression'."""
#!/usr/bin/env python3 # noqa:E265

from brain_games.engine import control_game
from brain_games.games import progression


def main():
    """Start the game 'Progression'."""
    control_game(progression)


if __name__ == '__main__':
    main()
