# Difference between variable and properties
#variable is assin the value or ....> no validation
# propertres of get and set

#properties of get and set
class name():
 
  @property
  def name(self):
    self._name()

    #set 
    @ name._setter
    def name(self,value):
      if value >=20:
        self.name=10
      else:
        self.name=value

      


# difference between variable and properties

def main():
    name=string=input("enter the name:")
    if name==0:
     print("name is valid")
    else:
       print("name is in valid")

    if __name__ == "__main__":
        main()
    
        