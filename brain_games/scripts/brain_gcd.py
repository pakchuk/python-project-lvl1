"""Script for start a game 'GCD'."""
#!/usr/bin/env python3 # noqa:E265

import brain_games.engine
import brain_games.games.gcd


def main():
    """Start a game 'GCD'."""
    brain_games.engine.logic(brain_games.games.gcd.make_game_dataset())

    if __name__ == '__main__':
        main()
