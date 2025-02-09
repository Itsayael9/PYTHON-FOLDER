x=float(input("entrer le 1er nombre : "))
y=float(input("entrer le 2eme nombre : "))

def division(x,y):
    try:
      return x/y
    except ZeroDivisionError:
        return "la division sur 0 est pas possible "
print(division(x,y))

    