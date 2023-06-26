import uuid
import signup

premiumUserCollection = []
userCollection = []
basicUserCollection = []


def updateUsers():
    for user in premiumUserCollection:
        if user not in userCollection:
            userCollection.append(user)
    for user in basicUserCollection:
        if user not in userCollection:
            userCollection.append(user)


def findUser(userName):
    for user in userCollection:
        if user.userName == userName:
            return user
    return None


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
    def __init__(self, name, userName, password):
        self.id = uuid.uuid4()
        self.name = name
        self.userName = userName
        self.password = signup.encode(password)
        self.balance = 0
        self.tax = 0.9

    def updateBalance(self):
        moneyAmount = float(input("Insira quantos reais você deseja adicionar: \n"))
        moneyAmount = validateMoneyAmount(moneyAmount)
        if moneyAmount == False:
            print("Operação cancelada")
        else:
            print(
                f"Saldo antigo: R${self.balance:,.2f}\nNovo saldo: R${self.balance+moneyAmount:,.2f}"
            )
            self.balance += moneyAmount

    def updateData(self):
        flag = True
        newUserName = input("Insira o novo nome de usuário\n")
        for user in userCollection:
            if user.userName == newUserName:
                flag = False
        if flag == True:
            print("Nome de usuário trocado com sucesso")
            self.userName = newUserName
        else:
            print("Nome já existente")


class basicUser(User):
    def __init__(self, name, userName, password):
        super().__init__(name, userName, password)

    def becomePremium(self, balance):
        if balance >= 200:
            self.balance -= 200
            premiumUserCollection.append(
                premiumUser(
                    self.id,
                    self.name,
                    self.userName,
                    self.balance,
                    signup.decode(self.password),
                )
            )
            print("Plano premium vitalício ativado!\n")
            userCollection.remove(self)
            basicUserCollection.remove(self)
            updateUsers()
        else:
            print("Saldo insuficiente")


class premiumUser(User):
    def __init__(self, id, name, userName, balance, password):
        super().__init__(name, userName, password)
        self.id = id
        self.tax = 0.95
        self.balance = balance
