from GameAction import *
from GameResult import *

class Game():
    def __init__(self):
        self.Victories = {
            GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
            GameAction.Paper: [GameAction.Rock, GameAction.Spock],
            GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
            GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
            GameAction.Spock: [GameAction.Scissors, GameAction.Rock],
        }

        self.ActionMessages = {
            (GameAction.Rock, GameAction.Scissors): "Rock smashes scissors",
            (GameAction.Rock, GameAction.Lizard): "Rock crushes lizard",
            (GameAction.Paper, GameAction.Rock): "Paper covers rock",
            (GameAction.Paper, GameAction.Spock): "Paper disproves spock",
            (GameAction.Scissors, GameAction.Paper): "Scissors cuts paper",
            (GameAction.Scissors, GameAction.Lizard): "Scissors decapitates lizard",
            (GameAction.Lizard, GameAction.Spock): "Lizard poisons spock",
            (GameAction.Lizard, GameAction.Paper): "Lizard eats paper",
            (GameAction.Spock, GameAction.Scissors): "Spock smashes scissors",
            (GameAction.Spock, GameAction.Rock): "Spock vaporizes rock",
        }

        self.ResultMessages = {
            GameResult.Tie: "User and computer picked {action}. Draw game!",
            GameResult.Victory: "{message}. You won!",
            GameResult.Defeat: "{message}. You lost!"
        }

    def assess_game(self, user_action, computer_action):
        """
        Genera el resultado de la partida
        """
        if user_action == computer_action:
            print(self.ResultMessages[GameResult.Tie].format(action=user_action.name))
            return GameResult.Tie

        if (user_action, computer_action) in self.ActionMessages:
            message = self.ActionMessages[(user_action, computer_action)]
            print(self.ResultMessages[GameResult.Victory].format(message=message))
            return GameResult.Victory

        message = self.ActionMessages[(computer_action, user_action)]
        print(self.ResultMessages[GameResult.Defeat].format(message=message))
        return GameResult.Defeat


    def play_another_round(self):
        """
        Pregunta por consola si el jugador quiere seguir jugando
        """
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'