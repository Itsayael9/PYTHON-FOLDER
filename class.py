class Person:
  def __init__(self, name, age,date):
    self.name = name
    self.age = age
    self.date = date
   
  def get_name(self):
    return self.name
  def get_age(self):
    return self.age
  def get_date(self):
    return self.date
  def calculet_age(self):
    
    current_age = 2024
    age = current_age - int(self.date)
    print("your age  is ",age)

p1 = Person("John", 36 , "2005")
print(p1.get_name(), p1.get_age(),p1.get_date())

p2 = Person ("aya" , 19,"2000" )
print(p2.get_name(), p2.get_age(),p1.get_date()) 

p1.calculet_age()
p2.calculet_age()
