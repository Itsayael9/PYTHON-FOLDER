from datetime import datetime
import csv 

employee = [
    {"nom": "ahmad", "prenom": "jamal", "service": "HR", "section": "Recrutement", 
     "cadre": "Junior", "categorie": "B", "indice": 1, "echelon": 1, "ancientee": 10, 
     "date de naissance": "10/05/1995"},
    
    {"nom": "bakkali", "prenom": "manal", "service": "IT", "section": "Développement", 
     "cadre": "Senior", "categorie": "A", "indice": 3, "echelon": 1, "ancientee": 10, 
     "date de naissance": "15/07/1960"}
]

def calculer_age_retrait():
        global employee
        for emp in employee:
            date_naissance = emp["date de naissance"] 
    
            date_naissance = datetime.strptime(date_naissance, "%d/%m/%Y")
            now = datetime.now()
            age = now.year - date_naissance.year
            retirement_age = 60
            years_to_retire = retirement_age - age
            year_retrait = date_naissance.replace(year =now.year + years_to_retire) 
            
            emp["annes de retrait "] = year_retrait.year
            # l 'ajout de champ de age de retrait  dans le dictionnaire 
            if years_to_retire > 0:
                emp["age de retrait "] = year_retrait
            else:
                emp["age de retrait"] = 0  # ida kan mota9a3id deja           
            if years_to_retire >0 :
                return print("il vous rest ",years_to_retire,"ans pour votre retrait , et l'annes de retrait est ",year_retrait)
            else:
                return print("tu a deja dans l'age de retrait sa fait ",years_to_retire,"ans")
#appel de la fct calculer age de retrait     
print(calculer_age_retrait())
for emp in employee:
    print(emp)
#ala9damia 
def suivi_avancement():
    global employee
    for emp in employee:
        ancienite = emp["ancientee"]
        if ancienite>=10 :
            emp["indice"]+=1 #augmantation de l'indice
        elif ancienite>=5:
            emp["echelon"]+=1 #augmantation de l'echelon 
        else:
            print("pas de accremantation ni dans l'echelon ni dans l'indice")
#ajout de  echelle ou bieb indice sa depant de la ancienitee
print("voici le suivi d'avancement de ce employe : ")
print(suivi_avancement())

# Affichage des employés après le suivi d'avancement
for emp in employee:
    print(emp)

#dictioner au chaque employe difiner  un cle 
liste_conges = {
    "ahmad":[("01/01/2025","01/02/2025"),("03/04/2025","12/04/2025")],
    "manal":[("2024/02/10", "2024/02/15"),("2024/04/01", "2024/04/05")]
}
def ajouter_conge(nom_employe, date_debut, date_fin):
    if nom_employe in liste_conges:
        liste_conges[nom_employe].append((date_debut,date_fin))
    else :
        #creation d'une nv liste :
        liste_conges[nom_employe]=[(date_debut,date_fin)]
        print("conge ajouter pour  ",nom_employe,"de",date_debut,"jusqu'a",date_fin)
#appel de fct ajouter conjes e donner les valeur prevue 
print(ajouter_conge("rafi9a","12/12/2025","12/01/2025"))

#affichge de l'ajout de date de conges
print("affichage  le dictionnaire des conges ")
print(liste_conges)

def suivi_conges(liste_conges, fichier="C:\\Users\\pro\\Desktop\\python\\TPpython\\suivi_conges.txt"):#suivi conges pour les souvgarder dans un ficjier txt
    with open(fichier,"w")as file:
        file.write("NOM  : DATE DE DEBUT , DATE DE FIN \n")
        #enregistrement de chaque conges
        for nom, periodes in liste_conges.items():
            for periode in periodes:
                date_debut, date_fin = periode
                file.write(f"{nom}, {date_debut}, {date_fin}\n")
    print("les donnes de conges on etait suvrgarder dans le fichier suivi_conge")
#apel de la fct souvgarder les conges    
suivi_conges(liste_conges)   
#dictionnaire de liste de formation     
liste_formation = {
    "ahmad ":["devloppemnt digital"],
    "manal":["design digital"],
    "rafi9a ":["infrastructure digital "]
    
}
def suivi_formation(liste_formation,fichier="C:\\Users\\pro\\Desktop\\python\\TPpython\\suivi_formation.txt"):
    with open(fichier,"w") as file :
        for nom, formations in liste_formation.items():
            file.write(f"{nom} :")
            file.write(",".join(formations))
            file.write("\n")
    print("les donnes de formation on etait souvgarder dans le fichir txt ")
# appeel de fct     
suivi_formation(liste_formation)



#listes des salaires 
salaires = [
    {"nom": "Ahmad", "salaire_de_base": 7000, "cotisation": 1000, "prime": 500, "absence": 2},
    {"nom": "Manal", "salaire_de_base": 10000, "cotisation": 2000, "prime": 1000, "absence": 6},
    {"nom": "Rafi9a", "salaire_de_base": 5000, "cotisation": 400, "prime": 300, "absence": 1}
]

# fct pour calculer le salair net 
def calculer_salaire_net(salaire_base, cotisations, primes, absences):
    try:
        #l'operation de calcule de salaire net 
        salaire_per_day = salaire_base / 22
        salaire_absence = salaire_per_day * absences
        salaire_net = salaire_base + primes - cotisations - salaire_absence
        return salaire_net
    except Exception as e:
        print(f"Erreur lors du calcul du salaire net : {e}")
        return None

# creation de fichier csv 
def creer_fichier_csv(fichier="employes.csv"):
    try:
        with open(fichier, "w") as file:
            # ajouter le cle salaie net 
            writer = csv.DictWriter(file, fieldnames=["nom", "salaire_de_base", "cotisation", "prime", "absence", "salaire_net"])
            writer.writeheader()
            
            # le calcul de salair net de chaque employer par le boucle pour
            for employe in salaires:
                #gerer les exceptions avec try 
                try:
                    
                    if not all(key in employe for key in ["nom", "salaire_de_base", "cotisation", "prime", "absence"]):
                        print(f"Champs manquants pour l'employé {employe.get('nom', 'Inconnu')}.")
                        continue
                    
                    employe["salaire_net"] = calculer_salaire_net(
                        employe["salaire_de_base"],
                        employe["cotisation"],
                        employe["prime"],
                        employe["absence"]
                    )
                    
                    #ecriture de salire net dans le fichier 
                    if employe["salaire_net"] is not None:
                        writer.writerow(employe)
                    else:
                        print(f"Erreur : Salaire net non calculé pour {employe['nom']}.")
                #gere les exceptiond
                except Exception as e:
                    print(f"Erreur lors du traitement de l'employé {employe['nom']} : {e}")
        print("Le fichier CSV a été créé avec succès :", fichier)
    except Exception as e:
        print(f"Erreur lors de la création du fichier CSV : {e}")

# Appel de la fonction pour créer le fichier CSV
creer_fichier_csv("employes.csv")

# Affichage des salaires nets dans la console
for employe in salaires:
    print(f"{employe['nom']} : Salaire net = {employe['salaire_net']} DH")
    
#exercice 5 ;
historique_employes = {
    "Ahmad": {
        "promotions": [
            {"nouveau_poste": "Senior", "augmentation": 2000}
        ],
        "formations": [
            {"intitule": "Développement Digital"}
        ],
        "conges": [
            ("01/01/2025", "01/02/2025"),
            ("03/04/2025", "12/04/2025")
        ]
    },
    "Manal": {
        "promotions": [
            {"nouveau_poste": "Junior Developer", "augmentation": 1500}
        ],
        "formations": [
            {"intitule": "Infrastructure Digitale"}
        ],
        "conges": [
            ("2024/02/10", "2024/02/15"),
            ("2024/04/01", "2024/04/05")
        ]
    }
}

def afficher_historique(nom_employe):
    # Historique de l'employer
    historique = historique_employes[nom_employe]
    print(f"Historique de {nom_employe} :\n")

    # Affichage des promotions
    print("Promotions :")
    for promotion in historique["promotions"]:
        print(f"- Nouveau poste : {promotion['nouveau_poste']}, Augmentation : {promotion['augmentation']} DH")

    # Affichage des formations
    print("\nFormations :")
    for formation in historique["formations"]:
        print(f"institule : {formation['intitule']}")

    # Affichage des conges 
    print("\nconges ")
    for conge in historique["conges"]:
        print(f"debut de conges : {conge[0]}, fin de conges : {conge[1]}")

# Appels à la fonction
afficher_historique("Ahmad")
afficher_historique("Manal")



# Sauvegarde de l'historique des employés dans un fichier texte
with open("historique_employes.txt", "w") as file:
    for nom_employe, historique in historique_employes.items():
        file.write(f"{nom_employe}: Promotions: {historique['promotions']}  formations: {historique['formations']}  Conge: {historique['conges']}\n")

from datetime import datetime

# Liste des stagiaires avec les informations
liste_stagaires = [
    {"nom": "aya", "prenom": "elouahabi", "debut de stage": "12/12/2025", "fin de stage": "12/01/2026", "superviseur": "box3aib"},
    {"nom": "ahlam", "prenom": "mrini", "debut de stage": "12/12/2025", "fin de stage": "12/01/2026", "superviseur": "mohamed"}
]

# Fonction pour suivre les stagiaires et afficher leur temps restant
def suivie_stagiaires(liste_stagiaires):
   today = datetime.today() #date actuelle 
   for stagiaire in liste_stagiaires:
        fin_stage = datetime.strptime(stagiaire["fin de stage"], "%d/%m/%Y")# Conversion de la date de fin de stage en format datetime
        if today < fin_stage: #si le stage  il pas terminer 
            temps_restant = fin_stage - today  #operation pour calculer combien de temps rest pour terminer le stage 
            print(f"{stagiaire['prenom']} {stagiaire['nom']} Temps restant : {temps_restant.days} jours")
        else:
            print(f"{stagiaire['prenom']} {stagiaire['nom']} a terminé son stage.")  #si le stage a terminer c-a-d le resultat de opertaion est negative 
#apel de fct           
suivie_stagiaires(liste_stagaires)

#merci pour votre attention de aya elouahabi

    

    

    





        
    






    