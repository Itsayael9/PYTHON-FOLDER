import random #regeneration de code 
import csv #les fichier csv 
import json #fichier json 

# Dictionnaires 
produits = {}  # Dictionnaire des produits
clients = {}   # Dictionnaire des clients
client_produits = {}  # Dictionnaire des ventes de produits
panier = {}    # Panier d'achat 
num_client_counter = 1  # Compteur de numéro de client

def generer_code_produit():
   return random.randint(0, 100) #code produit aleatoire

def generer_code_acces(prenom):
    #mot de pass pour le client
    if len(prenom) < 2:      #etre surre que le prenom doit avoir ou moin 2 lettre 
        raise ValueError("Le prénom doit contenir au moins 2 lettres") # en cas d'antres moinn de 2 lettre retourner un message d'erreur (gestion des erreur ) 
    
    # Deux premières lettres du prénom en majuscules(upper)
    code_debut = prenom[:2].upper()
    
    # Nombre aléatoire entre 0 et 100
    code_number = random.randint(0, 100)
    
    return f"{code_debut}{code_number}"

def ajouter_produit(quantite):
    #Ajouter un nouveau produit au stock
    code_produit = generer_code_produit() 
    
    # S'assurer que le code de produit est unique
    while code_produit in produits: 
        code_produit = generer_code_produit()
    
    produits[code_produit] = quantite #ajouter un cle avec sa valeur dans le dictionnaire de produit 
    return code_produit 

def retirer_produit(code_produit, quantite):
    #retirer un produit du stock
    if code_produit not in produits:# kitaked wax dik produit deja kayn f dictionnaire 
        return False
    
    if produits[code_produit] < quantite:  #436 > 100 
        print("Quantité insuffisante en stock.")
        return False
    
    produits[code_produit] -= quantite #diminution de quantite de produit 
    return True

def supprimer_produit(code_produit):
   #supprimer un produit du stock
    if code_produit in produits:
        del produits[code_produit] #del pour supprimer une valeur dans le dictionnaire 
        return True
    return False

def ajouter_client(prenom):
    #ajouter un nouveau client 
    global num_client_counter
    
    # Générer un code d'accès
    code_acces = generer_code_acces(prenom)
    
    # Attribuer un numéro de client incrémental 
    num_client = num_client_counter 
    num_client_counter += 1     
    
    # Ajouter le client au dictionnaire
    clients[num_client] = code_acces
    return num_client, code_acces

def modifier_code_acces_client(num_client, nouveau_code):
    """Modifier le code d'accès d'un client"""
    if num_client in clients:
        clients[num_client] = nouveau_code
        return True
    return False

def supprimer_client(num_client):
    """Supprimer un client"""
    if num_client in clients:
        del clients[num_client]
        return True
    return False

def afficher_quantite_produit(code_produit):
    """Afficher la quantité disponible d'un produit a partir les getters """
    return produits.get(code_produit, 0)

def ajouter_au_panier(code_produit, quantite):
    """Ajouter un produit au panier"""
    if code_produit not in produits:
        print("Produit non trouvé.")
        return False
    
    if produits[code_produit] < quantite:
        print("Quantité insuffisante en stock.")
        return False
    
    # Ajouter au panier si le produit existe
    if code_produit in panier:
        panier[code_produit] += quantite
    else:
        panier[code_produit] = quantite
    
    return True

def retirer_du_panier(code_produit, quantite):
    """Retirer un produit du panier"""
    if code_produit not in panier:
        print("ce produit il n'existe pas dans le stocke .")
        return False
    
    if panier[code_produit] < quantite:
        print("Quantité dans le panier insuffisante.")
        return False
    
    panier[code_produit] -= quantite
    
    # Supprimer l'article si la quantité atteint zéro 
    if panier[code_produit] == 0:
        del panier[code_produit] 
    
    return True

def generer_recu(num_client):
    """ticket de recu total de l'achatt du client"""
    # Générer des prix aléatoires pour les produits 
    prix_produits = {code: round(random.uniform(1, 100), 2) for code in produits.keys()}
    
    recu = f"Reçu pour le client {num_client}\n"
    total = 0
    
    for code_produit, quantite in panier.items():
        prix = prix_produits.get(code_produit, 0)
        total_produit = prix * quantite
        recu += f"Produit {code_produit}: {quantite} x {prix}€ = {total_produit}€\n"
        total += total_produit
    
    recu += f"Total: {total}€"
    return recu 

def ecrire_fichier_csv(nom_fichier='clients.csv'):
    """Enregistrer les informations des clients dans un fichier CSV"""
    with open(nom_fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Numéro Client', 'Code Accès'])
        for num_client, code_acces in clients.items():
            writer.writerow([num_client, code_acces])

def ecrire_fichier_json(nom_fichier='produit_ventes.json'):
    """Enregistrer les informations de ventes de produits dans un fichier JSON"""
    with open(nom_fichier, 'w') as jsonfile:
        json.dump(client_produits, jsonfile, indent=4)

def menu_gerant():
    """Menu pour le gérant du magasin"""
    while True:
        print("\n--- Menu Gérant---")
        print("1. Ajouter un Produit")  
        print("2. Retirer une Quantité de Produit")
        print("3. Supprimer un Produit")
        print("4. Ajouter un Client")
        print("5. Modifier Code d'Accès Client")
        print("6. Supprimer un Client")
        print("7. Afficher Quantité Produit")
        print("8. Enregistrer Clients en CSV")
        print("9. Enregistrer Ventes en JSON")
        print("0. Quitter")
        
        choix = input("Votre choix: ")
        
        if choix == '1':
            quantite = int(input("Quantité du produit: "))
            code = ajouter_produit(quantite)
            print(f"Produit ajouté avec le code {code}")
        
        elif choix == '2':
            code = int(input("Code du produit: "))
            quantite = int(input("Quantité à retirer: "))
            retirer_produit(code, quantite) 
        
        elif choix == '3':
            code = int(input("Code du produit à supprimer: "))
            supprimer_produit(code)
        
        elif choix == '4':
            prenom = input("Prénom du client: ")
            num, code = ajouter_client(prenom)
            print(f"Client ajouté - Numéro: {num}, Code d'accès: {code}") 
        
        elif choix == '5':
            num = int(input("Numéro du client: "))
            nouveau_code = input("Nouveau code d'accès: ")
            modifier_code_acces_client(num, nouveau_code)
        
        elif choix == '6':
            num = int(input("Numéro du client à supprimer: "))
            supprimer_client(num)
        
        elif choix == '7':
            code = int(input("Code du produit: "))
            print(f"Quantité disponible: {afficher_quantite_produit(code)}")
        
        elif choix == '8':
            ecrire_fichier_csv()
            print("Clients enregistrés en CSV")
        
        elif choix == '9':
            ecrire_fichier_json()
            print("Ventes enregistrées en JSON")
        
        elif choix == '0':
            break
            #sortir de boucle 
        
        else:
            print("Choix invalide")

def menu_client(num_client, code_acces):
    """Menu pour le client"""
    while True:
        print("\n--- Menu Client ---")
        print("1. Modifier Code d'Accès")
        print("2. Afficher Quantité Produit")
        print("3. Ajouter au Panier")
        print("4. Retirer du Panier")
        print("5. Effectuer un Achat")
        print("0. Quitter")
        
        choix = input("Votre choix: ")
        
        if choix == '1':
            nouveau_code = input("Nouveau code d'accès: ")
            modifier_code_acces_client(num_client, nouveau_code)
            code_acces = nouveau_code
        
        elif choix == '2':
            code = int(input("Code du produit: "))
            print(f"Quantité disponible: {afficher_quantite_produit(code)}")
        
        elif choix == '3':
            code = int(input("Code du produit: "))
            quantite = int(input("Quantité à ajouter: "))
            ajouter_au_panier(code, quantite)
        
        elif choix == '4':
            code = int(input("Code du produit: "))
            quantite = int(input("Quantité à retirer: "))
            retirer_du_panier(code, quantite)
        
        elif choix == '5':
            recu = generer_recu(num_client)
            print(recu)
            
            # Mettre à jour le stock
            for code, quantite in panier.items():
                retirer_produit(code, quantite)
                
                # Mettre à jour les ventes totales
                client_produits[code] = client_produits.get(code, 0) + quantite
            
            # Vider le panier
            panier.clear()
        
        elif choix == '0':
            break
        
        else:
            print("Choix invalide")

def main():
    """Programme principal"""
    while True:
        print("\n--- Application de Gestion de Magasin ---")
        print("1. Gérant")
        print("2. Client")
        print("0. Quitter")
        
        role = input("Votre choix: ")
        
        if role == '1':
            menu_gerant()
        
        elif role == '2':
            num_client = int(input("Votre numéro de client: "))
            code_acces = input("Votre code d'accès: ")
            
            if num_client in clients and clients[num_client] == code_acces:
                menu_client(num_client, code_acces)
            else:
                print("Numéro de client ou code d'accès incorrect.")
        
        elif role == '0':
            break
        
        else:
            print("Choix invalide")

# Point d'entrée du programme
if __name__ == "__main__":
    main()