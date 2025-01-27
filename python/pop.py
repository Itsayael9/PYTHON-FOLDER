liste =[1,4,7,9,3,3,3,3,3,3,3,3,3]
aya = liste.pop(3)
print(liste)
print(aya)
longeur = len(liste)
print(longeur)
exist = 383 in liste
print(exist)
indice = liste.index(7)
print(indice)
compte = liste.count(10)
print(compte)
liste1= [1,2,3]
liste2=["a","b","c"]
liste2.extend(liste1)
print(liste2)
this_liste=[1,2,3,4]
my_list = this_liste.copy()
print(my_list)

liste = [ 1,2,3,4,5]
tuplee = tuple(liste)
print(tuplee)

mon_set ={1,2,3,4,5} 
mon_set.discard(2)
print(mon_set)