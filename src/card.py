from typing import Dict
import fjson

def add_card(card_name:str, card_desc:str, column_name:str, board_name:str, my_board:dict) -> bool:
    # my_board = board.get_board(board_name)
    my_board[column_name][card_name] = card_desc

    fjson.ecrire_json(my_board, board_name)
    print(f"La card {card_name} a été créée avec succès !")
    return True

def update_card(card_name:str, column_name:str, board_name:str, my_board:dict) -> bool:
    req = ""
    #Question d'entrée
    while req=="":
        print(f"Vous vouhaitez modifier cette card : {card_name}")
        req = input("Que voulez vous modifier ? (T pour Titre, D pour Description) ")
    
    #Modification Titre
    if req == "T":
        new_card_name = input("Choisissez un nouveau titre : ")
        old_card_desc = my_board[column_name].pop(card_name)
        my_board[column_name][new_card_name] = old_card_desc
        print(my_board)
        fjson.ecrire_json(my_board, board_name)
        print(f"Titre {card_name} modifié et remplacé par {new_card_name}")
        return True
    elif req == "D" :
        new_desc = input("Choisissez une nouvelle description : ")
        old_desc = my_board[column_name][card_name]
        my_board[column_name][card_name] = new_desc
        fjson.ecrire_json(my_board, board_name)
        print("Description modifiée")
        return True
    print("Mauvaise commande. Bye.")
    return False

def delete_card(card_name:str, column_name:str, board_name:str, my_board:dict) -> bool:
    resp = ""

    while resp =="":
        resp = input(f"Êtes-vous sûr de vouloir supprimer la card : {card_name} ? (Y pour oui, N pour non)")

    if resp=="Y" :
        my_board[column_name].pop(card_name)
        fjson.ecrire_json(my_board, board_name)
        print(f"La Card {card_name} est supprimée. Adios !")
        return True
    elif resp=="N":
        print("Ok. Bye.")
        return False
    print("Mauvaise commande. Bye.")
    return False

def get_card(card_name:str, column_name:str, board_name:str) -> Dict[str,str]:
    my_board = fjson.lire_json(board_name)
    card_desc = my_board[column_name][card_name]
    return (card_name, card_desc)