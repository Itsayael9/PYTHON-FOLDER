import csv

def creer_stock(chemin_fichier):
    stock = {}
    

    with open("partie.csv", mode='r') as file: 
            reader = csv.DictReader(file)
            for row in reader:
                
                code = row['code']
                stock[code] = {
                    'nom': row['nom'],
                    'prix': float(row['prix']),
                    'stock': int(row['stock'])
                }
    
    
    return stock 

def afficher_stock(stock):
    for code, info in stock.items():
        # Affichage simple, sans formatage complexe
        print(f"{code}   {info['nom']}   {info['prix']}   {info['stock']}")

