class Card:

    def __init__(self, house_input, num_input, valueOfCard_input):
        self.house = house_input
        self.num = num_input
        self.value = valueOfCard_input

    def __str__(self):
        return self.num + ' of ' + self.house

    def getValue(self):
        return self.value