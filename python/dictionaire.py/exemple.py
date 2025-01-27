inventaire = {
    "pommes": {"quantite": 50, "prix": 3},
    "bananes": {"quantite": 20, "prix": 2},
    "oranges": {"quantite": 30, "prix": 4},
}

def affichages_produit():
    if inventaire :
        for produit, detail in inventaire.items() :
            print(f"le produit :{produit}")
            print(f"la quantite :{detail["quantite"]}")
            print(f"le prix de produit :{detail["prix"]}")
            print("           ===============              ")
    else:
        print("le dictionnaire est vide ")
    
    

def ajouter_produit():
    nom = input("Entrez le nom du produit : ")
    quantite = int(input("Entrez la quantité : "))
    prix = int(input("Entrez le prix : "))
    inventaire[nom] = {"quantite": quantite, "prix": prix}
    print("Produit ajouté")
    affichages_produit()

def modification():
    affichages_produit()
    produit = input("Entrez le nom du produit : ")
    if produit in inventaire:
        quantite = int(input("Entrez la nouvelle quantité : "))
        inventaire[produit]["quantite"] = quantite
        print("Quantité modifiée")
        affichages_produit()
    else:
        print("Produit non trouvé")

def total():
    facture = 0
    for produit in inventaire:
        facture += inventaire[produit]["quantite"] * inventaire[produit]["prix"]
    print(f"Total : {facture} €")

def supprimer_produit():
    affichages_produit()
    produit = input("Entrez le nom du produit à supprimer : ")
    if produit in inventaire:
        del inventaire[produit]
        print("Produit supprimé")
        affichages_produit()
    else:
        print("Produit non trouvé")

def afficher_menu():
    while True:
        print("\nMenu :")
        print("1. Afficher les produits")
        print("2. Ajouter un produit")
        print("3. Modifier une quantité")
        print("4. Voir le total")
        print("5. Supprimer un produit")
        print("6. Quitter")
        
        choix = input("Votre choix : ")
        
        if choix == "1":
            affichages_produit()
        elif choix == "2":
            ajouter_produit()
        elif choix == "3":
            modification()
        elif choix == "4":
            total()
        elif choix == "5":
            supprimer_produit()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide")

afficher_menu()