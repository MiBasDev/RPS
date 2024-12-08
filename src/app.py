from GameAction import *
from GameResult import *

Victories = {
    GameAction.Rock: GameAction.Scissors,
    GameAction.Paper: GameAction.Rock,
    GameAction.Scissors: GameAction.Paper
}

ActionMessages = {
    (GameAction.Rock, GameAction.Scissors): "Rock smashes scissors",
    (GameAction.Paper, GameAction.Rock): "Paper covers rock",
    (GameAction.Scissors, GameAction.Paper): "Scissors cuts paper"
}

ResultMessages = {
    GameResult.Tie: "User and computer picked {action}. Draw game!",
    GameResult.Victory: "{message}. You won!",
    GameResult.Defeat: "{message}. You lost!"
}

def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(ResultMessages[GameResult.Tie].format(action=user_action.name))
        return GameResult.Tie

    if Victories[user_action] == computer_action:
        message = ActionMessages[(user_action, computer_action)]
        print(ResultMessages[GameResult.Victory].format(message=message))
        return GameResult.Victory

    message = ActionMessages[(computer_action, user_action)]
    print(ResultMessages[GameResult.Defeat].format(message=message))
    return GameResult.Defeat


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break

if __name__  == '__main__':
    main()