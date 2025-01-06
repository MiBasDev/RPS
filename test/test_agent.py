import pytest
from src.Agent import Agent
from src.GameAction import GameAction
from unittest.mock import patch

@pytest.fixture
def agent():
    return Agent()

@pytest.mark.agent
def test_no_history(agent):
    """
    Si no hay historial, la función debe retornar 'Paper'.
    """
    predicted_action = GameAction.Rock
    agent.action_history = {action: 0 for action in GameAction}  # Sin historial
    counter_action = agent.get_best_counter_action(predicted_action)
    assert counter_action == GameAction.Paper

@pytest.mark.agent
def test_repeated_player_action(agent):
    """
    Si el jugador repite la misma acción dos veces, debe retornar una acción aleatoria.
    """
    agent.player_action_history = [GameAction.Rock, GameAction.Rock]  # Jugada repetida
    predicted_action = GameAction.Paper
    with patch("random.choice", return_value=GameAction.Scissors):  # Mock del random
        counter_action = agent.get_best_counter_action(predicted_action)
        assert counter_action == GameAction.Scissors

@pytest.mark.agent
def test_valid_counter_action(agent):
    """
    Si hay un historial válido y una jugada vence a la predicción, retorna esa jugada.
    """
    predicted_action = GameAction.Scissors
    agent.action_history = {action: 5 for action in GameAction}  # Historial válido
    with patch("random.choice", side_effect=[GameAction.Rock]):  # Mock del random
        counter_action = agent.get_best_counter_action(predicted_action)
        assert counter_action == GameAction.Rock  # Rock vence a Scissors

@pytest.mark.agent
def test_no_possible_counter_action(agent):
    """
    Si no hay contrajugadas posibles calculadas, retorna una acción por defecto.
    """
    predicted_action = GameAction.Lizard
    agent.action_history = {action: 0 for action in GameAction}  # Sin historial válido
    agent.player_action_history = []
    
    counter_action = agent.get_best_counter_action(predicted_action)
    assert counter_action == GameAction.Paper  # Refleja el comportamiento actual
