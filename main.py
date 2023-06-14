# imports necessários para rodar o programa
from card import Card
import signin
import signup


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
                    pass
                case "VENDA":
                    pass
                case "ADM":
                    print("TU é o bichão memo hein doido")
                    break
                case "SAIR":
                    break
                case "LOGOUT":
                    print("Obrigado por contar conosco")
                    self.currentUser = None
                # Caso a entrada não exista nas opções
                case _:
                    print("Não entendi o que quis dizer")


