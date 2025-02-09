import csv
# lecture de fichiere csv 
with open("files_py/file.csv","r") as fichier :
    contenu = fichier.read()
#afficher le contenu    
    print(contenu)
    