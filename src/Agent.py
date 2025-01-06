import random
from src.GameAction import GameAction
from src.GameResult import GameResult
from src.Game import Game

class Agent():
    def __init__(self):
        # Historial de jugadas del agente
        self.action_history = {action: 0 for action in GameAction}
        # Historial de jugadas del jugador
        self.player_action_history = []
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
                    - result["losses"] * 2  # Penalizar si hemos perdido mucho contra esta
                    + result["wins"] # Favorecer si ganamos contra esta
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
        if len(self.player_action_history) > 1:
            if self.player_action_history[0] == self.player_action_history[1]:
                return random.choice(list(GameAction))
        
        posible_plays = []
        for agent_action, winning_actions in Game().Victories.items():
            if predicted_action in winning_actions:
                if sum(self.action_history.values()) != 0:
                    posible_plays.append(agent_action)
                else:
                    return GameAction.Paper 
        
        return random.choice(posible_plays)

    def update_history(self, agent_action, result, player_action):
        """
        Actualiza el historial del jugador y los resultados de la partida.
        """
        if agent_action in self.action_history:
            self.action_history[agent_action] += 1
        
        self.player_action_history = [player_action] + self.player_action_history

        # Actualizar resultados
        if result == GameResult.Defeat:
            self.result_history[agent_action]["wins"] += 1
        elif result == GameResult.Victory:
            self.result_history[agent_action]["losses"] += 1
        elif result == GameResult.Tie:
            self.result_history[agent_action]["ties"] += 1