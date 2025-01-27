def est_palindrome(T):
    i, j = 0 ,len(T) - 1
    
    while i < j:
        if T[i] != T[j]:
            return False
        i += 1
        j -= 1
    return True


T = []
n = int(input("Combien d'éléments voulez-vous entrer dans le tableau ? "))
for i in range(n):
    valeur = int(input(f"Entrez la valeur de l'indice  {i+1}: "))
    T.append(valeur)


if est_palindrome(T):
    print("Le tableau est un palindrome.")
else:
    print("Le tableau n'est pas un palindrome.")

