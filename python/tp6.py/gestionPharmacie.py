import csv
import json

stock = {}
commande  = []
livraison = []
medicament = []

chemin = "stoc12k.csv"

try : 
        with open( chemin,'r', encoding = 'utf8') as file :
            reader = csv.DictReader(file)  
            for i in reader :
                stock[i['code']] = {
                    'nom' : i['nom'],
                    'price' : float(i['prix']),
                    'stock' : int(i['stock']),
                }   

except FileNotFoundError :
    print("Le fichier n'a pas été trouvé.")

def sauvegarder_stock():
    with open(chemin, 'w', encoding='utf8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['code', 'nom', 'prix', 'stock'])
        writer.writeheader()
        for code, i in stock.items():
            writer.writerow({'code': code, 'nom': i['nom'], 'prix': i['price'], 'stock': i['stock']})

def affichage_du_stock(stock):
    print("Code        Nom                  Prix             Stock     ")
    print("---------------------------------------------------------------")
    for code, i in stock.items():
        print(f"{code}         {i['nom']}               {i['price']}        {i['stock']}")
        print("---------------------------------------------------------------")
affichage_du_stock(stock)

def maj_stock(stock, code, quantite) :
    nv = stock[code]['stock'] + quantite
    stock[code]['stock'] = nv
    print ("produit modifier")
    sauvegarder_stock()

def creer_commande(stock):
    while True : 
        code = input("entrer le code de produit ")
        if code in stock:
            quantite = int(input(f"entrer la quantite de produit{stock[code]['nom']} : "))
            if  stock[code]['stock'] >= quantite: 
                commande.append((code, quantite))
                print("Commande ajoutée")
                stock[code]['stock'] -= quantite
                sauvegarder_stock()
            else : 
                print("Quantité invalide")
        else :
            print("Le code du produit n'existe pas.")
        print("Voulez-vous ajouter un autre produit à votre commande? (o/n)")
        choice = input()
        if choice!= "o":
            break      
    return commande

def calculer_montant(stock , commande):
    total = 0 
    for code, quantite in commande :
        total += stock[code]['price'] * quantite
        print(f"Produit : {stock[code]['nom']}  Quantité : {quantite}  Montant : {total}")
chemin1 = 'livraison.json'
def ajouter_json(x):
    with open (chemin1 , 'a' ) as file :
        json.dump(x, file , indent=4)
        file.write('\n')


medicament.append(stock)
ajouter_json(medicament)



    
         
        
    
def menu():
    while True:
        print("\nMenu:")
        print("1. Modifier le stock")
        print("2. creer une commande ")
        print("3. Afficher le stock")        
        print("5. Quitter ")
        choix = input("Votre choix : ")
        if choix == "1" :
            code = input("Entrez le code du produit à modifier : ")
            if code in stock:
                quantite = int(input("Entrez la quantité à ajouter : "))
                maj_stock(stock, code, quantite)
            else:
                print("Le code du produit n'existe pas.")
        elif choix == "2" :
            
            commande = creer_commande (stock)
            calculer_montant(stock , commande)
        elif choix == "3" :
            
            affichage_du_stock(stock)
        elif choix == "5" :
            print("Au revoir!")
            break
menu()