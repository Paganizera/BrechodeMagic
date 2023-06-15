import uuid
import signup

premiumUserCollection = []
userCollection = []
basicUserCollection = []

def updateUsers():
    userCollection.update(basicUser,premiumUserCollection)
    

def validateMoneyAmount(moneyAmount):
    if moneyAmount < 0:
        newAmount = float(
            input(
                "Valor insuficiente, favor inserir uma quantia válida ou digite 0 para cancelar"
            )
        )
        return validateMoneyAmount(newAmount)
    elif moneyAmount == 0:
        return False
    else:
        return moneyAmount


class User:
    def __init__(self, name, username, password):
        self.id = uuid.uuid4()
        self.name = name
        self.username = username
        self.password = signup.encode(password)
        self.balance = 0

    def updateBalance(self):
        moneyAmount = float(input("Insira quantos reais você deseja adicionar: "))
        moneyAmount = validateMoneyAmount(moneyAmount)
        if moneyAmount == False:
            print("Operação cancelada")
        else:
            print(
                f"Saldo antigo: R${self.balance:,.2f}\nNovo saldo: R${self.balance+moneyAmount:,.2f}"
            )
            self.balance += moneyAmount


class basicUser(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)

    def becomePremium(self, balance):
        if balance >= 200:
            self.balance -= 200
            premiumUserCollection.update(
                premiumUser(self.id, self.name, signup.decode(self.password))
            )
            del self
        else:
            print("Saldo insuficiente")


class premiumUser(User):
    def __init__(self, id, name, username, password):
        super().__init__(name, username, password)
        self.id = id


basicUserCollection.append(basicUser("BATATA", "senha"))
