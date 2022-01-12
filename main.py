from player import Player, Human, Cpu

while True:
    numberOfPlayers, numberOfCPU = input("Enter the number of human players and cpu players, separated by a space bar "
                                         "in between (max 4 combined): ").split()

    if not numberOfPlayers.isdigit() or not numberOfCPU.isdigit():
        print("Sorry, the numbers you have typed are not positive integers. Please try again.")
        continue
    elif (int(numberOfPlayers) + int(numberOfCPU)) > 4:
        print("Sorry, too many players. Please try again.")
        continue
    elif (int(numberOfPlayers) + int(numberOfCPU)) == 1:
        print("Sorry, too little players. Please try again.")
    else:
        break

playerList = []

humanIndex = 1

for human_player in range(int(numberOfPlayers)):
    name = input("Please enter Player " + str(humanIndex) + "'s name: ")
    ownCards = list()
    initialise = Human(name, ownCards)
    playerList.append(initialise)

    humanIndex += 1

cpuIndex = 1

for cpu_player in range(int(numberOfCPU)):
    cpuNumber = cpuIndex
    ownCards = list()
    initialise = Cpu(cpuNumber, ownCards)
    playerList.append(initialise)

    cpuIndex += 1

for player in range(len(playerList)):
    playerList[player].drawCard()
    playerList[player].drawCard()
    playerList[player].aceAction()

    print(playerList[player].formattedOutcome())

print("")

for player in range(len(playerList)):

    if isinstance(playerList[player], Human):

        while True:

            if playerList[player].totalValue() == 21:
                print("Congrats, " + playerList[player].name + "! You've hit blackjack in your first round. ")
                break

            option = input(playerList[player].humanName() + ", would you like to stand (s) or hit (h)? ")

            if option != 's' and option != 'h':
                print("Sorry, the option you have chosen is invalid. Please try again.")
                continue
            elif option == 'h':
                playerList[player].drawCard()
                playerList[player].aceAction()

                if playerList[player].totalValue() < 21:
                    print(playerList[player].formattedOutcome())
                    continue
                elif playerList[player].totalValue() == 21:
                    print(playerList[player].formattedOutcome())
                    print("You've hit blackjack, congratulations!")
                    break
                else:
                    print(playerList[player].formattedOutcome())
                    print("Sorry, you've busted.")
                    break
            else:
                break
    elif isinstance(playerList[player], Cpu):

        while playerList[player].totalValue() < 17:

            playerList[player].drawCard()
            playerList[player].aceAction()

print("")

for player in range(len(playerList)):
    print(playerList[player].formattedOutcome())