"""Script for start a game 'GCD'."""
#!/usr/bin/env python3 # noqa:E265

from brain_games.engine import control_game
from brain_games.games import gcd


def main():
    """Start the game 'GCD'."""
    control_game(gcd)


if __name__ == '__main__':
    main()
