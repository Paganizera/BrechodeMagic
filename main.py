from card import Card
from setup import *
from user import *


class Main:
    def __init__(self):
        self.currentUser = None
        initalSetup()
        self.session(self.currentUser)

    def session(self, uid):
        print("\nSeja bem vindo(a)\n")
        while True:
            print("O que deseja fazer?\n")
            if uid:
                print(
                    "Alterar Dados (dado)\nVender Carta (venda)\nDepósito (deposito)\nConsultar Saldo (saldo)\nFazer LogOut (logout)"
                )
                if type(uid) == basicUser:
                    print("Tornar-se premium (premium)")
            else:
                print("Cadastrar-se (cadastro)\nLogin (login)")

            print("Consultar Carta (consulta)\nEncerrar programa (sair)\n")

            mode = input().upper()
            match str(mode):
                case "CONSULTA":
                    self.SEARCHSCREEN()
                case "SAIR":
                    break
                case "CADASTRO":
                    if not uid:
                        self.SIGNUP()
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "LOGIN":
                    if not uid:
                        uid = self.SIGNIN()
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "PREMIUM":
                    if type(uid) == basicUser:
                        validate = input(
                            "Para se tornar Premium é necessário R$200.00\nDeseja proceder? (S/N)\n"
                        )
                        print()
                        if validate.upper() == "S":
                            userName = uid.userName
                            uid.becomePremium(uid.balance)
                            for card in availableCardList:
                                if card.owner == uid:
                                    availableCardList.remove(card)
                            del uid
                            uid = findUser(userName)
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "DADO":
                    if uid:
                        uid.updateData()
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "VENDA":
                    if uid:
                        self.INSTANTIATECARD(uid)
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "DEPOSITO":
                    if uid:
                        uid.updateBalance()
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "SALDO":
                    if uid:
                        print(f"Seu saldo é: R${uid.balance}")
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case "LOGOUT":
                    if uid:
                        print("Obrigado por contar conosco\n")
                        uid = None
                    else:
                        print("\nNão entendi o que quis dizer\n")
                case _:
                    print("\nNão entendi o que quis dizer\n")

    def SIGNUP(self):
        def validatePassword(password, passwordConfirm):
            if password != passwordConfirm:
                print("\nSenhas não correspondem, tente novamente\n ")
                password = input("Insira uma senha:\n")
                passwordConfirm = input("Insira uma senha:\n")
                return password, passwordConfirm
            return password, passwordConfirm

        def validateName(name):
            if len(name) > 50:
                newName = input(
                    "\nA entrada excedeu o limite de caracteres (50)\nTente novamente:\n"
                )
                return validateName(newName)
            return name

        def validateUserName(userName):
            existUser = findUser(userName)
            if existUser:
                newUserName = input(
                    "\nNome de usuário já cadastrado, por favor, insira outro nome\n"
                )
                return validateUserName(newUserName)
            return userName

        print("\nSeja bem vindo à tela de Cadastro!\n")
        name = input("Insira seu nome completo:\n")
        name = validateName(name)
        userName = input("Insira seu nome de usuário:\n")
        userName = validateUserName(userName)
        password = input("Insira uma senha:\n")
        passwordConfirm = input("Confirme a senha:\n")
        password, passwordConfirm = validatePassword(password, passwordConfirm)
        basicUserCollection.append(basicUser(name, userName, password))
        updateUsers()

    def SIGNIN(self):
        while True:
            userName = input("\nInsira o seu nome de usuário:\n")
            currentUser = findUser(userName)
            password = input("Digite sua senha\n")
            if currentUser:
                if password == signup.decode(currentUser.password):
                    self.currentUser = currentUser
                    print("Logado com sucesso!\n")
                    return currentUser
                else:
                    print("Informações inválidas")
                    validate = input("Deseja tentar novamente? (S/N)\n")
                    if validate == "s".capitalize():
                        return self.SIGNIN()
            else:
                print("Informações inválidas")
                validate = input("Deseja tentar novamente? (S/N)\n")
                if validate == "s".capitalize():
                    return self.SIGNIN()

    def INSTANTIATECARD(self, currentuser):
        while True:
            print("\nSeja bem vindo. Segue em anexo as cartas disponíveis\n")
            for card in cardList:
                print(card)
            card = input("Digite o nome da carta:\n")
            cardName = findCard(card)
            if cardName == None:
                validate = input(
                    "Nome de carta inválido. Deseja tentar novamente:(S/N)\n"
                )
                if validate == "n".capitalize():
                    break
            else:
                price = round(float(input("Insira o preço de venda da carta:\n")), 2)
                availableCardList.append(Card(card, currentuser, price))
                break

    def SEARCHSCREEN(self):
        print("\nSeja bem vindo(a) a tela de Busca!\n")
        while True:
            print("\nO que deseja exibir?\n")
            searchmode = input(
                "Toda a Loja (tudo)\nBusca por da carta (nome)\nBusca por estoque de usuario (usuario)\nSair (sair)\n"
            )
            match searchmode.upper():
                case "TUDO":
                    for i in range(len(availableCardList)):
                        print(
                            i + 1,
                            " - ",
                            availableCardList[i].name,
                            availableCardList[i].price,
                        )
                    if self.currentUser:
                        validate = input("Deseja comprar alguma carta? (S/N)\n")
                        if validate == "S":
                            cardId = input("Qual o número da carta desejada?\n")
                            self.BUYCARD(availableCardList[int(cardId) - 1])
                case "NOME":
                    name = input("Digite o nome da carta que quer encontrar\n")
                    flag = False
                    availableCard = []
                    for carta in availableCardList:
                        if carta.name == name:
                            availableCard.append(carta)
                            flag = True
                    for i in range(len(availableCard)):
                        print(
                            i + 1,
                            " - ",
                            availableCard[i].name,
                            availableCard[i].price,
                        )
                    if flag == True:
                        if self.currentUser:
                            validate = input("Deseja comprar alguma carta? (S/N)\n")
                            if validate == "S":
                                cardId = input("Qual o número da carta desejada?\n")
                                self.BUYCARD(availableCard[int(cardId) - 1])
                    else:
                        print("Carta não encontrada ou estoque insuficiente\n")
                case "USUARIO":
                    flag = False
                    owner = input(
                        "Digite o nome do usuário que deseja consultar o estoque\n"
                    )
                    availableCard = []
                    for carta in availableCardList:
                        if carta.owner.name == owner:
                            availableCard.append(carta)
                            flag = True
                    for i in range(len(availableCard)):
                        print(
                            i + 1,
                            " - ",
                            availableCard[i].name,
                            availableCard[i].price,
                        )
                    if flag == True:
                        if self.currentUser:
                            validate = input("Deseja comprar alguma carta? (S/N)\n")
                            if validate == "S":
                                cardId = input("Qual o número da carta desejada?\n")
                                self.BUYCARD(availableCard[int(cardId) - 1])
                    else:
                        print("Usuário não encontrado ou cartas não existentes\n")
                case "SAIR":
                    break
                case _:
                    print("\nNão entendi o que quis dizer\n")

    def BUYCARD(self, card):
        if self.currentUser == card.owner:
            validate = input(
                "Você não pode comprar sua própria carta!\nDeseja retirá-la do estoque? (S/N)\n"
            )
            if validate.capitalize() == "S":
                availableCardList.remove(card)
                del card
        else:
            if self.currentUser.balance >= card.price:
                self.currentUser.balance -= int(card.price)
                card.owner.balance += card.owner.tax * int(card.price)
                availableCardList.remove(card)
                del card
            else:
                print("Saldo insuficiente\n")


main = Main()
