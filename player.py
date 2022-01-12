import random
from deck import Deck

class Player:

    def drawCard(self):
        self.getCard = random.choice(Deck.deck)
        Deck.deck.remove(self.getCard)
        self.cards.append(self.getCard)

    def totalValue(self):
        self.total = 0
        for eachCard in self.cards:
            self.total += eachCard.getValue()
        return self.total

    # def alternativeTotal(self):
    #
    #     if self.hasAce():
    #
    #         alternative_total = self.totalValue() - 10
    #         return " or " + str(alternative_total)
    #     else:
    #         return ""

    def hasAce(self):

        ace_counter = 0

        for card in self.cards:
            if card.num == 'A':
                ace_counter += 1

        if ace_counter > 0:
            return True
        else:
            return False

    def aceAction(self):

        if self.hasAce() and (self.totalValue() > 21):

            for card in self.cards:
                if card.num == 'A':
                    card.value = 1

                if self.totalValue() <= 21:
                    break

    def formattedOutcome(self):

        string = ""
        for cardName in self.cards:

            string += str(cardName)
            if self.cards.index(cardName) < (len(self.cards) - 2):
                string += ', '
            elif self.cards.index(cardName) == (len(self.cards) - 2):
                string += ' and '

        if isinstance(self, Human):
            if self.humanName()[-1] == 's':
                return self.humanName() + "' cards: " + string + ". Your current total is: " + str(self.totalValue())
            else:
                return self.humanName() + "'s cards: " + string + ". Your current total is: " + str(self.totalValue())
        else:
            return self.cpuName() + "'s cards: " + string + ". It's total is: " + str(self.totalValue())

class Human(Player):

    def __init__(self, humanName, personalCards):
        self.name = humanName
        self.cards = personalCards

    def humanName(self):
        return self.name


class Cpu(Player):

    def __init__(self, numberOfCpus, personalCards):
        self.number = numberOfCpus
        self.cards = personalCards

    def cpuName(self):
        return "CPU#" + str(self.number)