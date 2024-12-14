from GameAction import GameAction
from GameResult import GameResult
from Game import Game

class Agent():
    def __init__(self):
        # Historial de jugadas del jugador
        self.action_history = {action: 0 for action in GameAction}
        # Historial en base a los resultados
        self.result_history = {
            action: {"wins": 0, "losses": 0, "ties": 0} for action in GameAction
        }
        # Acción por defecto
        self.default_action = GameAction.Rock 

    def predict_player_action(self):
        """
        Predice la próxima jugada del jugador basándose en el historial de jugadas
        y los resultados obtenidos.
        """
        total_actions = sum(self.action_history.values())
        if total_actions == 0:
            return self.default_action

        # Calcular probabilidad 
        action_probabilities = {}
        for action, count in self.action_history.items():
            if count > 0:
                # Ponderar frecuencia de jugadas y evitar siempre la misma predicción
                result = self.result_history[action]
                score = (
                    count * 2  # Frecuencia base
                    - result["losses"]  # Penalizar si hemos perdido mucho contra esta
                    + result["wins"]  # Favorecer si ganamos contra esta
                )
                action_probabilities[action] = max(score, 1)  # Evitar puntuación 0
            else:
                action_probabilities[action] = 1  # Acción sin historial mínimo peso

        # Predicción basada en ponderación
        predicted_action = max(action_probabilities, key=action_probabilities.get)
        return predicted_action

    def get_best_counter_action(self, predicted_action):
        """
        Retorna la jugada que vence contra la acción predicha.
        """
        for agent_action, winning_action in Game().Victories.items():
            if winning_action == predicted_action:
                return agent_action
        return self.default_action 

    def update_history(self, player_action, result):
        """
        Actualiza el historial del jugador y los resultados de la partida.
        """
        if player_action in self.action_history:
            self.action_history[player_action] += 1

        # Actualizar resultados
        if result == GameResult.Victory:
            self.result_history[player_action]["wins"] += 1
        elif result == GameResult.Defeat:
            self.result_history[player_action]["losses"] += 1
        elif result == GameResult.Tie:
            self.result_history[player_action]["ties"] += 1