import uuid
import signup
class User:
    def __init__(self, name, password):
        self.id = uuid.uuid4()
        self.name=name
        self.password = signup.encode(password)
        self.balance = 0


class basicUser(User):
    def __init__(self,name, password):
        super().__init__(name, password)
     
class premiumUser(User):
      def __init__(self,name, password):
        super().__init__(name, password)
        
           
        
Batata = premiumUser("BATATA", "senha" )
print(Batata.name)
print(Batata.id)
print(Batata.password)
print(Batata.balance)