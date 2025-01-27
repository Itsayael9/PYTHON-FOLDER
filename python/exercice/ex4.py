n = int(input("combien de matiere tu a passer  ahmed ?"))
i=0
s=0
for i in range(n):
    note_ahmed = float(input("entre votre note "))
    s = note_ahmed +s  #la somme des notes de ahmad 

n = int(input("combien de matiere tu a passer  khalid ?"))
i=0
s1=0
for i in range(n): #de i jusqu'a les notes qui a paser 
    note_khalid = float(input("entre votre note "))
    s1 = note_khalid +s1
   

moyenne_ahmed = s/n
print("la moyenne de ahmed est :", moyenne_ahmed ) 

       
      

moyenne_khalid = s1/n
print("la moyenne de khalid est :", moyenne_khalid )

if moyenne_ahmed > moyenne_khalid :
    print("ahmed a la meilleur moyenne")
else:
    print("khalid a la meilleur moyenne")
    
    
        
        
    
        
  
  
    


    