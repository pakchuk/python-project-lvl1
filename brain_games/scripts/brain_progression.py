"""Script for start a game 'Progression'."""
#!/usr/bin/env python3 # noqa:E265

import brain_games.engine
import brain_games.games.progression


def main():
    """Start a game 'Progression'."""
    brain_games.engine.logic(brain_games.games.progression.make_game_dataset())

    if __name__ == '__main__':
        main()
