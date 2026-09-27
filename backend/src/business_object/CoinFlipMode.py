import random

from game import Game
from game_mode import GameMode
from player import Player


class CoinFlipMode(GameMode):
    """
    Mode de jeu basé sur le lancer d'une pièce de monnaie (Pile ou Face).
    """

    def play(self, p1: Player, p2: Player, choice: str) -> Game:
        """
        Exécute une partie de pile ou face.
        :param p1: Premier joueur
        :param p2: Second joueur
        :param choice: Le choix de p1 ("pile" ou "face")
        :return: L'objet Game mis à jour avec le résultat
        """
        # 1. Normalisation du choix du joueur
        p1_choice = choice.strip().lower()
        if p1_choice not in ["pile", "face"]:
            raise ValueError("Le choix doit être 'pile' ou 'face'.")

        # 2. Détermination automatique du choix de p2.  

        # 3. Simulation du lancer de la pièce
        resultat_lancer = random.choice(["pile", "face"])

        # 4. Initialisation d'une nouvelle instance de Game
        game = Game(player1=p1, player2=p2)

        # 5. Détermination du gagnant (Logique extraite de l'ancien GameService)
        if p1_choice == resultat_lancer:
            game.set_winner(p1)
            game.set_loser(p2)
        else:
            game.set_winner(p2)
            game.set_loser(p1)

        # Enregistre le statut de la partie (ex: "FINISHED") et le détail du lancer
        game.status = "FINISHED"
        game.details = f"Résultat du lancer : {resultat_lancer}."

        return game
