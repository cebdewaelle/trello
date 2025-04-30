import json
import os


REPERTOIRE = "data/"
EXTENSION = ".json"


def lire_json(nom_board: str) -> dict:
    """ Fonction de lecture du fichier json du board passé en paramètre

    Args:
        nom_board (str): nom du board à charger

    Returns:
        dict: Contenu du board
    """
    fic = REPERTOIRE + nom_board + EXTENSION

    if not os.path.exists(fic):
        print(f"Le board {nom_board} n'existe pas")
        return {}

    with open(fic, "r") as jf:
        return json.load(jf)


def ecrire_json(data: dict, nom_board: str) -> None:
    """ Fonction d'écriture du fichier json contenant le board en paramètre

    Args:
        data (dict): dictionnaire contenu du board
        nom_board (str): nom du board
    """
    fic = REPERTOIRE + nom_board + EXTENSION

    with open(fic, "w", encoding="utf-8") as jf:
        json.dump(data, jf, ensure_ascii=False, indent=4)


def renommer_json(ancien_nom_board: str, nouveau_nom_board: str) -> bool:
    """ Fonction de renommage d'un fichier json

    Args:
        ancien_nom_board (str): nom du board à modifier
        nouveau_nom_board (str): nom du board
    """
    old_fic = REPERTOIRE + ancien_nom_board + EXTENSION
    new_fic = REPERTOIRE + nouveau_nom_board + EXTENSION

    if not os.path.exists(old_fic):
        print(f"Le board {ancien_nom_board} n'existe pas")
        return False

    if os.path.exists(new_fic):
        print(f"Le board {nouveau_nom_board} existe déjà")
        return False

    os.rename(old_fic, new_fic)
    if os.path.exists(old_fic) or not os.path.exists(new_fic):
        print(f"Erreur lors du renommage")
        return False

    return True


test1 = {
    "todo":[
        { "Retour": "prendre le metro" },
        { "Manger": "manger les restes d'hier" },
        { "Dormir": "aller se coucher pas trop tard" }
    ],
    "doing": [
        { "Coder": "développer le trello"},
        { "Parler": "le moins possible" },
        { "Réfléchir": "le plus possible" }
    ],
    "done": [
        { "Déjeuner": "manger le plat apporté"}
    ],
    "archive": [
        { "Venir": "venir en métro le matin" }
    ]
}


# fic_data = lire_json("test1")


# print(test1["doing"])
# print(test1["done"])


# test1["done"].append(test1["doing"].pop(1))


# print(test1["doing"])
# print(test1["done"])


# ecrire_json(test1, "test1")


# print(fic_data)

# print(renommer_json("test1", "test2"))
