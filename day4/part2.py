import re

def checkForWinningNumbers(game, winningNumbers, ownedNumbers, numberOfCards):
    dictOfNumbers = {}
    numberOfWinningNumbers = 0
    winningNumbers = re.split(r'\s+', winningNumbers)
    for winningNumber in winningNumbers:
        if winningNumber != "":
            dictOfNumbers[winningNumber] = 1
    ownedNumbers = re.split(r'\s+', ownedNumbers)
    for ownedNumber in ownedNumbers:
        if ownedNumber in dictOfNumbers:
            numberOfWinningNumbers += 1
    if numberOfWinningNumbers == 0:
        print("For game " + str(game) + " you won 0 cards")
        return []
    else:
        if numberOfCards - game < numberOfWinningNumbers:
            numberOfWinningNumbers = numberOfCards - game
        listOfCardsGained = []
        for card in range(game+1, game + numberOfWinningNumbers + 1):
            listOfCardsGained.append(card)
        print("For game " + str(game) + " you won " + str(numberOfWinningNumbers) + " cards")
        return listOfCardsGained



def handleCard(stackOfCardsToCheck, alreadyCheckedCards, lines, numberOfCards, currentPositionInStack):
    if currentPositionInStack in alreadyCheckedCards:
        pass
        listOfCardsGained = alreadyCheckedCards[currentPositionInStack]
        stackOfCardsToCheck += listOfCardsGained
        numberOfCardsGained = len(listOfCardsGained)

    else:
        cardText = lines[currentPositionInStack]
        game, gameNumbers = cardText.split(":")
        game = int(re.split(r'\s+', game)[1])
        winningNumbers, ownedNumbers = gameNumbers.split("|")
        listOfCardsGained = checkForWinningNumbers(game, winningNumbers, ownedNumbers, numberOfCards)
        stackOfCardsToCheck += listOfCardsGained
        numberOfCardsGained = len(listOfCardsGained)
    return numberOfCardsGained, alreadyCheckedCards


def manageStackOfCards(stackOfCardsToCheck, alreadyCheckedCards, lines, numberOfCards):
    currentPositionInStack = 0
    stackLength = len(stackOfCardsToCheck)
    totalNumberOfCardsGained = 0
    while currentPositionInStack < stackLength:
        numberOfCardsGained, alreadyCheckedCards = handleCard(stackOfCardsToCheck, alreadyCheckedCards, lines, numberOfCards, stackOfCardsToCheck[currentPositionInStack] - 1)
        totalNumberOfCardsGained += numberOfCardsGained
        stackLength = len(stackOfCardsToCheck)
        currentPositionInStack += 1
    return totalNumberOfCardsGained

def parseLines(lines):
    numbers = 0
    stackOfCardsToCheck = []
    alreadyCheckedCards = {}
    numberOfCards = len(lines)
    numberOfCheckedCards = numberOfCards
    for lineNumber in range(1, numberOfCards + 1):
        stackOfCardsToCheck.append(lineNumber)
    numberOfCheckedCards += manageStackOfCards(stackOfCardsToCheck, alreadyCheckedCards, lines, numberOfCards)
    print(numberOfCheckedCards)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)

main()
