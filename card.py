import uuid

cardList = []
availableCardList = []

def findCard(cardName):
    for card in cardList:
        if card == cardName:
            return card
    return None


class Card:
    def __init__(self, name, owner, price):
        self.id = uuid.uuid4()
        self.name = name
        self.owner = owner
        self.price = price
