
class Student:
  school="Akirachix"
  def __init__(self,firstname,lastname,age,country):
   self.firstname=firstname
   self.lastname=lastname
   self.age=age
   self.country=country
  #def greet(self):
      #return f"Hello {self.name} welcome to {self.school}, how is {self.country}" 
  def full_name(self):
      return f"Hello your name is {self.firstname} {self.lastname}"
  def years_of_birth(self) :
      year_of_birth=2022-self.age   
      return f"Hello your age is {year_of_birth}"
  def your_initials(self):
      return f"Hello your initials are {self.firstname[0]} {self.lastname[0]}"    

list_a=[1,2,3,4,5]
list_b=[10,20,30,40,50]
list_c=list_a+list_b
print(list_c)
    