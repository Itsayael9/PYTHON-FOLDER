# Déclarer un dictionnaire vide
mon_dictionnaire = {}

# Fonction pour ajouter une paire clé-valeur
def ajouter_element():
    cle = input("Entrez la clé : ")
    valeur = input("Entrez la valeur : ")
    mon_dictionnaire[cle] = valeur
    print(f"'{cle}': '{valeur}' a été ajouté au dictionnaire.") 
    

# Fonction pour afficher le dictionnaire
def afficher_dictionnaire():
    if mon_dictionnaire: # si le dictionnaire est non vide
        print("Contenu du dictionnaire :")
        for cle, valeur in mon_dictionnaire.items():
            print(f"{cle}: {valeur}")
    else:
        print("Le dictionnaire est vide.")

# Fonction principale
def menu():
    while True:
        print("\nMenu :")
        print("1. Ajouter un élément")
        print("2. Afficher le dictionnaire")
        print("3. Quitter")
        
        choix = input("Choisissez une option (1/2/3) : ")
        
        if choix == "1":
            ajouter_element()
        elif choix == "2":
            afficher_dictionnaire()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

# Lancer le programme
menu()
