"""Script for start a game 'Progression'."""
#!/usr/bin/env python3 # noqa:E265

from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Start the game 'Progression'."""
    run_game(progression)


if __name__ == '__main__':
    main()
