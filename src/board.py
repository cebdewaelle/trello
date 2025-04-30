from typing import List, Dict
import json
import os
import fjson

# def add_board(board_name:str, board: List[Dict[Dict]]) -> List[Dict[str,Dict[str,str]]]:

def add_board(board_name:str) -> bool:
    board = [
        {
            "To Do":[]
        },
        {
            "Doing":[]
        },
        {
            "Done":[]
        }
    ]

    fjson.ecrire_json(board, board_name)
    
    print(f"Le Board {board_name} a été créé avec succès !")
    return True

def update_board(old_board_name:str) -> bool:
    req = ""
    #Question d'entrée
    while req=="":
        req = input("Que voulez vous modifier ? (T pour titre, C pour Colonne) ")
    
    #Modification Titre
    if req == "T":
        new_board_name = input("Choisissez un nouveau titre : ")
        fjson.renommer_json(old_board_name, new_board_name)
        print("Titre modifié")
        return True
    elif req == "C" :
        #colonne.update_colonne
        print("Colonne modifiée")
        return True
    return False

def delete_board(board_name:str) -> bool:
    fjson.supprimer_json(board_name)
    print("Board supprimé !")
    pass

def get_board(board_name:str) -> List[Dict[str,Dict[str,str]]]:
    return fjson.lire_json(board_name)

# def save_board(board_name:str, board: List[Dict[Dict]])->bool:
#     #appel fonction json creation fichier pour ecraser le précédent par celui ci
#     pass
