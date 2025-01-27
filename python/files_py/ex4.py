#ficher1
with open("ficher1.txt", "w") as fichier1:   
  fichier1.write("Ligne 1 du fichier 1\n")
  fichier1.write("Ligne 2 du fichier 1\n")
    
      #fichier2
with open("ficher2.txt", "w") as fichier2:
  fichier2.write("Ligne 1 du fichier 2\n")
  fichier2.write("Ligne 2 du fichier 2\n")
  
     #fusion dans un fichier3    
     
with open("ficher1.txt", "r") as fichier1 , open("ficher2.txt", "r") as fichier2 , open("ficher3.txt", "w") as fichier3:
       contenu1 = fichier1.read()
       contenu2 = fichier2.read()
       fichier3.write(contenu1)
       fichier3.write(contenu2)