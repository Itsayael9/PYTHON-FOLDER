import csv


total_ventes = 0

with open("files_py/file2.csv", "r") as file:
    lecteur = csv.DictReader(file)  
    for ligne in lecteur:
        total_ventes += int(ligne["ventes"])  


print(f"Le total des ventes pour l'année est de {total_ventes}")

