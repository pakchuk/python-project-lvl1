"""Script for start a game 'calculator'."""
#!/usr/bin/env python3 # noqa:E265

import brain_games.games.calc
import brain_games.games.engine


def main():
    """Start a game 'calculator'."""
    brain_games.games.engine.logic(brain_games.games.calc.calc())

    if __name__ == '__main__':
        main()
