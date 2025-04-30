from typing import Dict
import fjson


def add_board(board_name:str) -> bool:

    board = {
            "To Do":{}
        ,
            "Doing":{}
        ,
            "Done":{}    
    }

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
    return True

def get_board(board_name:str) -> Dict[str,Dict[str,str]]:
    return fjson.lire_json(board_name)
