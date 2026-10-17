from business_object.game import Game
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log
from utils.singleton import Singleton


class GameDao(metaclass= Singleton):
    """class containing methods to acces Games in the database."""

@log
def create(self, game) -> bool:
    """Create a game in the database.
    Args:
        Game to create
    Returns:
        True if creation is successful, False otherwise
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

    created = False
    if res:
        game.id_game = res["id_game"]
        created = True

    return created


@log
def find_by_id(self, id_game: int) -> Game:
    """Find a game by its id.
    Args:
        id_game (int): The ID of the game to find
    Returns:
        Game matching the given id, or None if not found
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

    game = None
    if res:
        game = Game(
            id_game=res["id_game"],
            id_player1=res["id_player1"],
            id_player2=res["id_player2"],
            game_mode=res["game_mode"],
            id_winner=res["id_winner"],
            detail=res["detail"],
            timestamp=res["timestamp"],
        )

    return game



@log
def find_all(self) -> list[Game]:
    """Find all games in the database.
    Returns:
        List of all games
    """
    try:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM project.game;"
                )
                res = cursor.fetchall()

    except Exception as e:
        logger.error(e)
        raise

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
        ([]).append(game)

    return []