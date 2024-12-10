from GameAction import *
from GameResult import *

class Game():
    def __init__(self):
        self.Victories = {
            GameAction.Rock: GameAction.Scissors,
            GameAction.Paper: GameAction.Rock,
            GameAction.Scissors: GameAction.Paper
        }

        self.ActionMessages = {
            (GameAction.Rock, GameAction.Scissors): "Rock smashes scissors",
            (GameAction.Paper, GameAction.Rock): "Paper covers rock",
            (GameAction.Scissors, GameAction.Paper): "Scissors cuts paper"
        }

        self.ResultMessages = {
            GameResult.Tie: "User and computer picked {action}. Draw game!",
            GameResult.Victory: "{message}. You won!",
            GameResult.Defeat: "{message}. You lost!"
        }

    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            print(self.ResultMessages[GameResult.Tie].format(action=user_action.name))
            return GameResult.Tie

        if self.Victories[user_action] == computer_action:
            message = self.ActionMessages[(user_action, computer_action)]
            print(self.ResultMessages[GameResult.Victory].format(message=message))
            return GameResult.Victory

        message = self.ActionMessages[(computer_action, user_action)]
        print(self.ResultMessages[GameResult.Defeat].format(message=message))
        return GameResult.Defeat


    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'