while True:
    print("Voici le menu de pizza :")
    print("1.Pizza petit 20 dh ")
    print("2.Pizza moyenne 35 dh ")
    print("3.Pizza grande 75 dh ")

    taille_pizza = str(input("Entrer la taille de la pizza : "))
    nbr_pizza = int(input("Entrer le nombre de pizza : "))
    extra_fromage = str(input("Voulez-vous de l'extra fromage oui/non : "))

    def calcul_prix_pizza():
        if taille_pizza == "petit":
            return (20 * nbr_pizza)
        elif taille_pizza == "moyenne":
            return (35 * nbr_pizza)
        elif taille_pizza == "grande":
            return (75 * nbr_pizza)

    
    prix_base = calcul_prix_pizza()
    prix_extra_fromage = 0

    
    if extra_fromage == "oui":
        prix_extra_fromage = 8 * nbr_pizza

    total = prix_base + prix_extra_fromage

    #  la facture
    print("  FACTURE ")
    print(f"Taille de pizza : {taille_pizza}")
    print(f"Nombre de pizzas : {nbr_pizza}")
    print(f"Prix base : {prix_base} dh")
    if extra_fromage == "oui":   
        print(f"Extra fromage : {prix_extra_fromage} dh")
    print(f"Total à payer : {total} dh")
    
    continuer = input(" un autre client ? (oui/non) : ")
    if continuer != "oui":  #si l'utilisateur a ecrir non alors on sort de la boucle
        print("Merci et à bientôt!")
        break
    
    
    
  
  

          
  
        
    
    

       
    