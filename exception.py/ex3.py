#conversion de chaine  de caracter en entier 
def convertir_en_entier(chaine):
    try:
        entier = int(chaine)
        return entier
    except ValueError:
        raise ValueError("Erreur : La chaîne ne peut pas être convertie en entier.")

# Exemple d'utilisation
chaine = input("Entrez une chaîne à convertir en entier : ")
try:
    print(convertir_en_entier(chaine))
except ValueError as e:
    print(e)