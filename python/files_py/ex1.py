#lecture de contenu de fichier
with open("files_py/file.txt","r") as fichier :
    contenu = fichier.read()
#afficher le contenu    
    print(contenu)