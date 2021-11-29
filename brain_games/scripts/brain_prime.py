"""Script for start a game 'Prime'."""
#!/usr/bin/env python3 # noqa:E265

import brain_games.engine
import brain_games.games.prime


def main():
    """Start a game 'Prime'."""
    brain_games.engine.logic(brain_games.games.prime.make_game_dataset())

    if __name__ == '__main__':
        main()
