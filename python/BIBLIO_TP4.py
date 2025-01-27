# Dictionnaires 
stock = {
    "123456789": {"Titre": "learn Python", "Auteur": "John ", "Quantite": 10},
    "987654321": {"Titre": "Algorithmes ", "Auteur": "michael", "Quantite": 5}
}


utilisateurs ={}  



# fct pour ajouter un livre :
def ajouterLivre(titre , auteur , ISBN, quantite ):
    if ISBN in stock:
        #ida kan deja ktab f stock 
        print(f"Erreur : Le livre avec l'ISBN {ISBN} existe déjà dans le stock.")
    else:
        # ida maknxi ktanb f stock
        stock[ISBN] = {"Titre": titre, "Auteur": auteur, "Quantite": quantite}
        print(f"Le livre '{titre}' a été ajouté au stock avec {quantite} livres .") 
        
def supprimerLivre(ISBN):
    if ISBN in stock :
        livre_supprimer = stock.pop(ISBN)
        print("le livre a etait supprimer")
    else :
        print("le livre n'exist pas dans le stock ")
 #tslif d ktab mnn biblio        
def emprunterLivre(ISBN, utilisateur):
    try:
    
        if ISBN in stock :
            #na9as mn quantite de livre f stock     
            stock[ISBN]["Quantite"] -= 1
            print(f"L'utilisateur '{utilisateur}' a emprunté le livre '{stock[ISBN]['Titre']}'.")
            print(f"Stock restant pour ce livre : {stock[ISBN]['Quantite']} exemplaires.")#affichage 
        else:
            print("le livre n'exist pas dans le stock ")
    except ValueError:
        print("la quantite que tu a dommander est pas disponible ")    
        
def retournerLivre(livres, ISBN, utilisateur, emprunts):
    for emprunt in emprunts:
        if emprunt["isbn"] == ISBN and emprunt["utilisateur"] == utilisateur:
            livres[ISBN]["quantite"] += 1 
            # emprunts.remove(emprunt)
            print(f"Livre retourné avec succès par {utilisateur}.") 
            return 
    print("Aucun emprunt correspondant trouvé.")
    
#si user t3atal mayrod ktab = mokhalafa 
    
def calculerAmande(nombre_jours_retard, tarif_journalier=1):
    if nombre_jours_retard > 0:
        A=  nombre_jours_retard * tarif_journalier
        return A
    
    
    elif nombre_jours_retard <0 :
        print("pas d'amande ")


def rechercherLivre(titre):
    
    trouve = False
    for ISBN, details in stock.items():
        if titre in details["Titre"]:
            print(f"Trouvé: ISBN: {ISBN}, Titre: {details['Titre']}, Auteur: {details['Auteur']}, Quantité: {details['Quantite']}")
            trouve = True
    if not trouve:
        print("Aucun livre correspondant trouvé.")

#statistique de livre 
def statistiquesLivres():
    total_livres = sum(details["Quantite"] for details in stock.values())
    print("-- STATISTIQUES --")
    print(f"Nombre total de livres: {len(stock)}")
    print(f"Nombre total d'exemplaires: {total_livres}") # xhal mn ktab kyna f wahed naw3 
    
        
def ajouterUtilisateur():
    # utilisateur = {
    #     "nom": nom,
    #     "prenom": prenom,
    #     "numero_carte": numero_carte
    # }
    # utilisateurs.append(utilisateur)
    nom = input("entrer votre nom ")
    prenom = input("entrer votre prenom ")
    numero_carte = input("entre le numero de votre carte  suetes ")

    
    utilisateurs["nom"]=nom
    utilisateurs["prenom"]=prenom
    utilisateurs["numero_carte"]=numero_carte
    print(f"nom:{nom} prenom {prenom} cart:{numero_carte} a etait ajoutr ")
    
    
def supprimerUtilisateur(numero_carte):
    for utilisateur in utilisateurs:
        if utilisateur["NumeroCarte"] == numero_carte:
            utilisateurs.remove(utilisateur)
            print(f"L'utilisateur avec le numéro de carte {numero_carte} a été supprimé.")
            return
    print("Utilisateur introuvable.")



        
def afficherStock() :
    def afficherStock():
        if not stock:
            print("Le stock est vide.")
        else:
            print("-- STOCK ACTUEL --")
            for ISBN, details in stock.items():
                print(f"ISBN: {ISBN}, Titre: {details['Titre']}, Auteur: {details['Auteur']}, Quantité: {details['Quantite']}")
                
    
    
    
    
    
    
    
                        ######################afichage#############################
def affichage():
    while True:
        print("MENU DE LA BIBLIOTHEQUE :")
        print("1.ajouter un livre ")
        print("2.supprimer un livre ")
        print("3.emprunterLivre")
        print("4.retourner le livrer ")
        print("5.calculer amande ")
        print("7.rechercher un livre ")
        print("8.ajouter utilisateur ")
        print("9.supprimer utilisateur ")
        print("10. Aficher le stock actuel")
        
    
        choix = input("entre le numero de votre choix :")
        
        if choix=="1":
            #ajouter un livre 
            titre = input("titre de livvre :")
            auteur = input("auteur de live :")
            ISBN = input("ISBN :")
            quantite = int(input("quantite de livre :"))
            
            ajouterLivre(titre , auteur , ISBN, quantite )  
        
        elif choix == "2":
            ISBN = input("entrer le titre de livre a supprimer :")
            supprimerLivre(ISBN)  
            
        elif choix == "4":
            # Afficher le stock
            afficherStock()
            
        elif choix=="5":
                 
            jours_retard = int(input("Nombre de jours de retard : "))
            amande = calculerAmande(jours_retard)
            print(f"Montant de l'amende : {amande} euros")
            
        elif choix == "6":
            titre = input("Titre du livre à rechercher : ")
            rechercherLivre(titre)

        elif choix == "7":
            statistiquesLivres()
        
        elif choix=="8":
            
            ajouterUtilisateur()
        
        elif choix == "9":
            numero_carte = input("Numéro de carte de l'utilisateur à supprimer : ")
            supprimerUtilisateur(numero_carte)

        elif choix == "10":
            afficherStock()
            
        else:
            print("choix invalider , essayer de repeter votre choix :")                
if __name__ == "__main__":
        affichage() 