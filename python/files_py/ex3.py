import json
data = [
    {
        "nom": "pomme",
        "prix": 10,
        "quantite": 11
    },
    {
        "nom": "banane",
        "prix": 15,
        "quantite": 10
    }
]
# lecture des données dans un fichier JSON
with open("fichier.json", "w") as fichier:
    json.dump(data, fichier, indent=4)    

with open ("fichier.json","r") as fichier:
    data = json.load(fichier)
    
    for dt in data:
        print(f"Nom: {dt['nom']}, {dt['prix']}, {dt['quantite']}")    
