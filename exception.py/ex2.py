my_fichier = input("Entrez le nom du fichier: ")
def lecture_fichier(my_fichier):
    try:
        with open(my_fichier, 'r') as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print("Le fichier ",my_fichier," n'existe pas.")

lecture_fichier(my_fichier)

