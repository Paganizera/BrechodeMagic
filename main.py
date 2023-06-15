# imports necessários para rodar o programa
from card import Card
import signin
import signup
from user import *


# Criando a classe main, que servirá como "servidor" do programa
class Main:
    # Complila este trecho ao iniciar
    def __init__(self):
        # A aplicação começa sem usuário logado
        self.currentUser = None
        # A sessão começa
        self.session(self.currentUser)

    # Descrição do método sessão, note que o parâmetro uid é usado
    # Ele se refere ao ID do usuário caso ele esteja logado
    def session(self, uid):
        print("Seja bem vindo(a)")
        # Para manter o site ativo até o usuário "fechar a página"
        while True:
            # Opções para todos users
            print(
                "O que deseja fazer\nConsultar Carta (consulta)\nEncerrar programa (sair)"
            )
            # Opções que só aparecem se existe um UID atívo
            if uid:
                # Opções exclusivas do admin
                if uid == "ADMIN":
                    print("Zona de Admininstração (adm)")
                # Opções somente para usuários cadastrados e logados

                print("Vender Carta (venda)\nFazer LogOut (logout)")

                # Escolha da funcionalidade

            mode = input().upper()
            # Acesso à funcionalidade escolhida
            match str(mode):
                case "CONSULTA":
                    self.SEARCHSCREEN()
                case "VENDA":
                    if uid:
                        self.INSTANTIATECARD()
                    else:
                        print("Não entendi o que quis dizer")
                case "ADM":
                    if uid == "ADMIN":
                        self.ADMINSCREEN()
                    else:
                        print("Não entendi o que quis dizer")
                    break
                case "SAIR":
                    break
                case "CADASTRO":
                    if not uid:
                        self.SIGNUP()
                    else:
                        print("Não entendi o que quis dizer")
                case "LOGIN":
                    if not uid:
                        self.SIGNIN()
                    else:
                        print("Não entendi o que quis dizer")
                case "LOGOUT":
                    if uid:
                        print("Obrigado por contar conosco")
                        self.currentUser = None
                    else:
                        print("Não entendi o que quis dizer")

                # Caso a entrada não exista nas opções
                case _:
                    print("Não entendi o que quis dizer")

    def SIGNUP(self):
        def validatePassword(password, passwordConfirm):
            if password != passwordConfirm:
                print("Senhas não correspondem, tente novamente\n ")
                password = input("Insira uma senha:\n")
                passwordConfirm = input("Insira uma senha:\n")
                return password, passwordConfirm
            return password, passwordConfirm

        def validateName(name):
            if len(name) > 0:
                if len(name) > 50:
                    newName = input(
                        "A entrada excedeu o limite de caracteres (50)\nTente novamente:\n"
                    )
                    return validateName(newName)
                return name
            newName = input("O tamanho da entrada não pode ser 0\nTente novamente:\n")

        print("Seja bem vindo à tela de Cadastro!")
        name = input("Insira seu nome completo:\n")
        name = validateName(name)
        userName = input("Insira seu nome completo:\n")
        userName = validateName(userName)
        password = input("Insira uma senha:\n")
        passwordConfirm = input("Insira uma senha:\n")
        password, passwordConfirm = validatePassword(password, passwordConfirm)
        basicUserCollection.append(basicUser(name, userName, password))
        updateUsers()

    def findUser(uid):
        flag = False
        for user in userCollection:
            if user.id == uid:
                return user
        if flag == False:
            print("Usuário não encontrado, deseja tentar novamente?")


main = Main()
