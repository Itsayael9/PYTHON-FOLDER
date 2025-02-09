import random
def devenir_ce_nombre():
    devenir_ce_nombre=random.randint(1,100)
    tentative=0 
    
    while True:
     try:
            deviner = int(input("deviner un nombre entre 1 et 100 "))
            tentative+=1
        
            if deviner<devenir_ce_nombre:
                print("plus haut")
            elif deviner>devenir_ce_nombre:
                print("plus petit")
            else:
                print(f"Bravo ! Vous avez trouvé en {tentative} tentatives.")
                break    
     except ValueError:
       print("svp enter un nbr valider")
     
devenir_ce_nombre() 
     

    
    
    
    
        
         

            
