
voyelles = "aeiouyAEIOUY"

phrase =input("Entrez une phrase : ")

nbr_voyelles = 0
nbr_consonnes = 0


for lettre in phrase:
  
    if lettre.isalpha():
     
        if lettre in voyelles:
            nbr_voyelles += 1
        else:
          nbr_consonnes += 1
    
          
print("Nombre de voyelles :", nbr_voyelles)
print("Nombre de consonnes :", nbr_consonnes)


    
          
