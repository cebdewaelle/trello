import board


def create_colonne(board: dict, nom_colonne: str) -> dict:
    board[nom_colonne] = {}
    return board


def update_colonne(board: dict, old_nom_colonne: str, new_nom_colonne: str) -> dict:
    board[new_nom_colonne] = board.pop(old_nom_colonne)
    return board


def delete_colonne(board: dict, nom_colonne: str) -> dict:
    del board[nom_colonne]
    return board


def afficher_colonne(board: dict, nom_colonne: str) -> None:
    print(board.get(nom_colonne))


