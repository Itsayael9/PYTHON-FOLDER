from datetime import datetime

employee = [
    {"nom": "Smith", "prenom": "Alice", "service": "HR", "section": "Recrutement", 
     "cadre": "Junior", "categorie": "B", "indice": 1, "echelon": 1, "ancientee": 10, 
     "date de naissance": "10/05/1995"},
    
    {"nom": "Doe", "prenom": "John", "service": "IT", "section": "Développement", 
     "cadre": "Senior", "categorie": "A", "indice": 3, "echelon": 1, "ancientee": 10, 
     "date de naissance": "15/07/1960"}
]

def calculer_age_retrait():
        global employee
        for emp in employee:
            date_naissance = emp["date de naissance"] 
            date_naissance = datetime.strptime(date_naissance, "%d/%m/%Y")  # Convertir la date en format datetime
            now = datetime.now()
            age = now.year - date_naissance.year  # Calcul de l'âge
            retirement_age = 60  # Âge de la retraite
            years_to_retire = retirement_age - age  # Calcul des années restantes avant la retraite
            year_retrait = date_naissance.replace(year=now.year + years_to_retire)  # Année de la retraite
            
            emp["annees de retraite"] = year_retrait.year  # Ajout de l'année de retraite dans le dictionnaire 
            if years_to_retire > 0:
                emp["age de retraite"] = year_retrait  # Ajout de l'âge de retraite
                print(f"il vous reste {years_to_retire} ans pour votre retrait, et l'année de retrait est {year_retrait.year}")
            else:
                emp["age de retraite"] = 0  # Si l'employé est déjà en retraite
                print(f"tu es déjà dans l'âge de retrait, il reste {years_to_retire} ans")

# Appel de la fonction pour calculer l'âge de retraite
print(calculer_age_retrait())
for emp in employee:
    print(emp)

# Fonction de suivi de l'avancement
def suivi_avancement():
    global employee
    for emp in employee:
        ancienite = emp["ancientee"]
        if ancienite >= 10:
            emp["indice"] += 1  # Augmentation de l'indice
            print(f"{emp['nom']} {emp['prenom']} a reçu une augmentation de l'indice.")
        elif ancienite >= 5:
            emp["echelon"] += 1  # Promotion d'échelon
            print(f"{emp['nom']} {emp['prenom']} a reçu une promotion d'échelon.")
        else:
            print(f"Pas d'augmentation pour {emp['nom']} {emp['prenom']}.")

# Appel de la fonction de suivi d'avancement
print("Voici le suivi d'avancement des employés :")
suivi_avancement()

# Affichage des employés après le suivi d'avancement
for emp in employee:
    print(emp)


# Dictionnaire des congés
conges = {
    "ahmad": [("01/01/2025", "01/02/2025"), ("03/04/2025", "12/04/2025")],
    "manal": [("2024/02/10", "2024/02/15"), ("2024/04/01", "2024/04/05")]
}

def ajouter_conge(nom_employe, date_debut, date_fin):
    if nom_employe in conges:
        conges[nom_employe].append((date_debut, date_fin))  # Ajout des dates de congé à la liste
        print(f"Congé ajouté pour {nom_employe} du {date_debut} au {date_fin}")
    else:
        conges[nom_employe] = [(date_debut, date_fin)]  # Création de la liste des congés si l'employé n'existe pas
        print(f"Congé ajouté pour {nom_employe} du {date_debut} au {date_fin}")

# Appel de la fonction ajouter_conge
print(ajouter_conge("rafi9a", "12/12/2025", "12/01/2025"))
print(ajouter_conge("ahmad", "01/02/2025", "12/04/2025"))

# Affichage du dictionnaire des congés
print("\nDictionnaire des congés :")
print(conges)
