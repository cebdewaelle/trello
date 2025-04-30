import board

def start()->None:
    print("BIENVENUE SUR TRELLO")
    while True :
        print("MENU")
        print("1 - Créer un board")
        print("2 - Modifier un board")
        print("3 - Afficher un board")
        print("4 - Quitter")

        choix = input("Choisissez une option 1-2-3-4")

        if choix == "1" :
            nom_board = input("Choisissez le nom de votre board : ")
            board.add_board(nom_board)
        elif choix == "2" :
            nom_board = input("Quel board souhaitez vous modifier ?")
            board.update_board(nom_board)
        elif choix == "3" :
            nom_board = input("Quel board souhaitez vous afficher ?")
            print(board.get_board(nom_board))
        elif choix == "4" :
            print("Adios")
            break
        else :
            print("Choix invalide, réessayez")