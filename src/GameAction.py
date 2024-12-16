from enum import IntEnum

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


def get_computer_action(agent):
    """
    Obtiene la jugada del ordenador
    """
    # Intentar predecir la jugada del jugador
    predicted_action = agent.predict_player_action()

    # El seleccionar jugada en base a la predicción
    computer_action = agent.get_best_counter_action(predicted_action)

    #print(f"[Agent predict: {predicted_action.name} -> Counter: {computer_action.name}]")
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    """
    Obtiene la jugada del jugador
    """
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    return GameAction(user_selection)
