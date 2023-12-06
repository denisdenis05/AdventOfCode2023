import re

def checkForWinningNumbers(game, winningNumbers, ownedNumbers):
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
        return 0
    else:
        return pow(2, numberOfWinningNumbers - 1)


def parseLines(lines):
    numbers = 0
    for line in lines:
        game, gameNumbers = line.split(":")
        game = int(re.split(r'\s+', game)[1])
        winningNumbers, ownedNumbers = gameNumbers.split("|")
        numbers += checkForWinningNumbers(game, winningNumbers, ownedNumbers)
        print("Game: " + str(game)+ " has " + str(numbers) + " winning numbers")
    print(numbers)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)

main()
