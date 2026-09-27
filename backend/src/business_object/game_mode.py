from abc import ABC, abstractmethod

from game import Game
from player import Player


class GameMode(ABC):
    @abstractmethod
    def play(self, p1: Player, p2: Player, **kwargs) -> Game:
        pass



