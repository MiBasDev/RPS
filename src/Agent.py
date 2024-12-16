import random
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
                    - result["losses"] * 1.5  # Penalizar si hemos perdido mucho contra esta
                    + result["wins"] * 1.2 # Favorecer si ganamos contra esta
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
        for agent_action, winning_actions in Game().Victories.items():
            if predicted_action in winning_actions:
                return random.choice(winning_actions)
        return self.default_action 

    def update_history(self, agent_action, result):
        """
        Actualiza el historial del jugador y los resultados de la partida.
        """
        if agent_action in self.action_history:
            self.action_history[agent_action] += 1

        # Actualizar resultados
        if result == GameResult.Defeat:
            self.result_history[agent_action]["wins"] += 1
        elif result == GameResult.Victory:
            self.result_history[agent_action]["losses"] += 1
        elif result == GameResult.Tie:
            self.result_history[agent_action]["ties"] += 1
        
        print(self.result_history)