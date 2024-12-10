from Game import Game
from GameAction import *

def main():
    game = Game()
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        game.assess_game(user_action, computer_action)

        if not game.play_another_round():
            break

if __name__  == '__main__':
    main()