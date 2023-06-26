from card import *
from user import *


def initalSetup():
    BATATA = basicUser("BATATA", "BATATA", "senha")
    VENDEDOR = basicUser("VENDEDOR", "VENDEDOR", "1")
    basicUserCollection.append(BATATA)
    basicUserCollection.append(VENDEDOR)
    availableCardList.append(Card("Planície", VENDEDOR, 23.34))
    availableCardList.append(Card("Atraxa", VENDEDOR, 23.34))
    availableCardList.append(Card("Arena Phyrexiana", BATATA, 23.34))
    availableCardList.append(Card("Adeus", VENDEDOR, 23.34))
    availableCardList.append(Card("Adeus", VENDEDOR, 43.34))
    availableCardList.append(Card("Adeus", VENDEDOR, 55.34))
    availableCardList.append(Card("Adeus", VENDEDOR, 23.34))

    cardList.append("Elesh Norn, Mãe das Máquinas")
    cardList.append("Planície")
    cardList.append("Atraxa, Grande Unificadora")
    cardList.append("Arena Phyrexiana")
    cardList.append("Adeus")

    updateUsers()
