#class student
#get_full name


#class__student
class studentsdata():
    def __init__(self, firstname, lastname,age,Gender):
        self.firstname= firstname
        self.lastname=lastname
        self.age=age
        self.Gender=Gender

#get_fullname
    def get_fullname(self):
      if self.Gender=='Male':
          print(f"Mr.{self.firstname} {self.lastname}")
      elif self.Gender=="female":
          print(f"ms.{self.firstname}{self.lastname}")
      else:
          print(f"{self.firstname}{self.lastname}")

      print(f"{self.firstname} {self.lastname} {self.age} {self.Gender}")

student1= studentsdata("naga","mora","24","Male")
student1.get_fullname()
    

        




          
    

    

    

    
    

    
    
      


      

    
    

