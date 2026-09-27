class GameModeFactory:
    """Fabrique responsable de créer l'objet GameMode correspondant."""

    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """Returns the corresponding GameMode object.

        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').

        Returns:
            GameMode: An instance of a class implementing GameMode.

        Raises:
            ValueError: If the requested game_mode is not supported.
        """
        if game_mode == "dice":
            return DiceMode()
        elif game_mode == "coinflip":
            return CoinFlipMode()
        else:
            raise ValueError(f"Mode de jeu non supporté : {game_mode}")
