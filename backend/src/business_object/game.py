from datetime import datetime

from typing import Optional

from player import Player


class Game:
    def __init__(
        self,
        player1: Player,
        player2: Player,
        game_mode: str,
        winner: Optional[Player],
        description: str,
        timestamp: datetime,
        ) -> None:
        self.id_game = Optional[int]= None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp


    def __str__(self) -> str:
        """Retourne une représentation lisible de la partie."""
        if self.winner is None:
            return f"{self.game_mode} between {self.player1} and {self.player2}. Draw"
        return f"{self.game_mode}
