import board
import fjson as js


def create_colonne(board: dict, nom_colonne: str, nom_board: str) -> dict:
    board[nom_colonne] = {}
    save_colonne(board, nom_board)
    return board


def update_colonne(board: dict, nom_board: str, old_nom_colonne: str, new_nom_colonne: str) -> dict:
    board[new_nom_colonne] = board.pop(old_nom_colonne)
    save_colonne(board, nom_board)
    return board


def delete_colonne(board: dict, nom_board: str, nom_colonne: str) -> dict:
    del board[nom_colonne]
    save_colonne(board, nom_board)
    return board


def afficher_colonne(board: dict, nom_colonne: str) -> None:
    print(board.get(nom_colonne))


def save_colonne(board: dict, nom_board: str,) -> None:
    js.ecrire_json(board, nom_board)
