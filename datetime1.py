from datetime import date

# Demander à l'utilisateur d'entrer une date
date_input = input("Entrez une date (au format YYYY-MM-DD) : ")

# Diviser la chaîne et extraire l'année, le mois, le jour
date_parts = date_input.split('-') 
#separe la date input par des tires 
year = int(date_parts[0]) #1er indice 
month = int(date_parts[1])#2emme indice 
day = int(date_parts[2])#3eme indice 

# Créer un objet date à partir de l'entrée de l'utilisateur
entered_date = date(year, month, day)

# Obtenir la date actuelle
current_date = date.today()

# Comparer les dates
if entered_date > current_date: #ida knat date li dakhal user kbira mn la date actuelle 
    print("La date entrée est dans le futur.")
elif entered_date < current_date:     #ida kant date li dakhal user sghira mn date actuelle 
    print("La date entrée est dans le passé.")
else:
    print("La date entrée est aujourd'hui.")  #si entred_date == current_date