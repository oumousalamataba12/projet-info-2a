
import random
from datetime import datetime

from game import Game
from game_mode import GameMode
from player import Player


class DiceMode(GameMode):
    def play(self, p1: Player, p2: Player, **kwargs) -> Game:
        """
        Cette méthode implémente un DiceMode
        -------
        Parameters:
        p1 (Player): The id of the player1
        p2 (Player): The id of the player2
        ---------
        Returns
        Game:  La partie jouée avec le gagnant renseigné

        """
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        if roll1 > roll2:
            winner = p1
        elif roll2 > roll1:
            winner = p2
        else:
            winner = None

        description = f"{p1} rolled {roll1}, {p2} rolled {roll2}."

        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description=description,
            timestamp=datetime.now(),
        )
