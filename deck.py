from card import Card

class Deck:
    houses = ['Diamonds', 'Clovers', 'Hearts', 'Spades']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    deck = []

    for house in houses:
        for num in numbers:

            if num == 'A':
                valueOfCard = 11
            elif num in ['J', 'Q', 'K']:
                valueOfCard = 10
            else:
                valueOfCard = int(num)

            deck.append(Card(house, num, valueOfCard))