voyelles = "aeiouyAEIOUY"

phrase =input("Entrez une phrase : ")


def compter_voyelells(phrase):
    nbr_voyelles = 0
    for lettre in phrase :
        if lettre.isalpha():
     
            if lettre in voyelles:
               nbr_voyelles += 1
    return nbr_voyelles 
                
      
      
print("Nombre de voyelles :", compter_voyelells(phrase))   
            