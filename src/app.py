from Game import Game
from GameAction import *
from Agent import *

def main():
    game = Game()
    agent = Agent()
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue
        
        computer_action = get_computer_action(agent)

        result = game.assess_game(user_action, computer_action)

        # Guardar en el historial
        agent.update_history(computer_action, result, user_action)

        if not game.play_another_round():
            break

if __name__  == '__main__':
    main()