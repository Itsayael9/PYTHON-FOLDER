
class AgeInvalideError(Exception):
   def __init__(self, age):
        super().__init__(f"Erreur : L'âge '{age}' est invalide. L'âge doit être entre 0 et 120.")

def verifierAge(age):
    if not (0 <= age <= 120):
        raise AgeInvalideError(age)
    print(f"L'âge {age} est valide.")


try:
    age = int(input("Entrez un âge : "))
    verifierAge(age)
except AgeInvalideError as e:
    print(e)
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")
