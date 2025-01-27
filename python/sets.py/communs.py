def commun(s1,s2):
    for item in s1 :
        if item in s2:
            return True
    return False

s1 = {1,2,3,4,5,6}
s2 = {2,8,9,0,56}

print(commun(s1,s2))