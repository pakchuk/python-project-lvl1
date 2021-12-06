"""Script for start a game 'check even'."""
#!/usr/bin/env python3 # noqa:E265

from brain_games.engine import control_game
from brain_games.games import check_even


def main():
    """Start the game 'check even'."""
    control_game(check_even)


if __name__ == '__main__':
    main()
