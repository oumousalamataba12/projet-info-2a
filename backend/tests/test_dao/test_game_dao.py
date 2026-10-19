
from unittest.mock import MagicMock, patch

from dao.game_dao import GameDao


def test_find_by_id_returns_game():
    fake_row = {
        "id_game": 10,
        "id_player1": 1,
        "id_player2": 2,
        "game_mode": "coinflip",
        "id_winner": 1,
        "detail": "Player 1 won",
        "timestamp": None,
    }

    fake_cursor = MagicMock()
    fake_cursor.fetchone.return_value = fake_row

    fake_connection = MagicMock()
    fake_connection.cursor.return_value.__enter__.return_value = fake_cursor

    with patch("dao.game_dao.DBConnection") as mock_db:
        mock_db.return_value.connection.__enter__.return_value = fake_connection

        game = GameDao().find_by_id(10)

    assert game.id_game == 10
    assert game.id_player1 == 1
    assert game.id_player2 == 2
    assert game.game_mode == "coinflip"
