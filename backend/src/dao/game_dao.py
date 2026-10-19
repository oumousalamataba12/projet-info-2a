from business_object.game import Game
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log
from utils.singleton import Singleton


logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    """Class containing methods to access games in the database."""

    @log
    def create(self, game: Game) -> bool:
        """Create a game in the database.

        Args:
            game: Game to create.

        Returns:
            True if creation is successful, False otherwise.
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO project.game "
                        "(id_player1, id_player2, game_mode, id_winner, detail) "
                        "VALUES "
                        "(%(id_player1)s, %(id_player2)s, %(game_mode)s, "
                        "%(id_winner)s, %(detail)s) "
                        "RETURNING id_game;",
                        {
                            "id_player1": game.id_player1,
                            "id_player2": game.id_player2,
                            "game_mode": game.game_mode,
                            "id_winner": game.id_winner,
                            "detail": game.detail,
                        },
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logger.error(e)
            raise

        if res:
            game.id_game = res["id_game"]
            return True

        return False

    @log
    def find_by_id(self, id_game: int) -> Game | None:
        """Find a game by its ID.

        Args:
            id_game: ID of the game to find.

        Returns:
            The matching Game, or None if not found.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "
                        "FROM project.game "
                        "WHERE id_game = %(id_game)s;",
                        {"id_game": id_game},
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logger.error(e)
            raise

        if not res:
            return None

        return Game(
            id_game=res["id_game"],
            id_player1=res["id_player1"],
            id_player2=res["id_player2"],
            game_mode=res["game_mode"],
            id_winner=res["id_winner"],
            detail=res["detail"],
            timestamp=res["timestamp"],
        )

    @log
    def find_all(self) -> list[Game]:
        """Find all games in the database.

        Returns:
            A list containing all games.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM project.game;")
                    res = cursor.fetchall()

        except Exception as e:
            logger.error(e)
            raise

        games = []

        for row in res:
            game = Game(
                id_game=row["id_game"],
                id_player1=row["id_player1"],
                id_player2=row["id_player2"],
                game_mode=row["game_mode"],
                id_winner=row["id_winner"],
                detail=row["detail"],
                timestamp=row["timestamp"],
            )
            games.append(game)

        return games