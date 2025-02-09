HT = float(input("ENTRERE LE PRIX DE HT "))
NA =int(input("entrer le nombre d'articl "))
TVA =float( input("entrer la valeur de tva "))

TTC = NA *HT*(1 +TVA / 100)

print("VOICI LE PRIX TOTAL TTC ",TTC) 