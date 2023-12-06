
def checkForAdjacentStar(currentLine, previousLine, nextLine, startOfNumber, endOfNumber):
    if startOfNumber > 0 and previousLine[startOfNumber-1] == "*":
        return True, "previous", startOfNumber - 1
    if endOfNumber < len(currentLine) - 1 and previousLine[endOfNumber+1] == "*":
        return True, "previous", endOfNumber + 1
    if startOfNumber > 0 and nextLine[startOfNumber-1] == "*":
        return True, "next", startOfNumber - 1
    if endOfNumber < len(currentLine) - 1 and nextLine[endOfNumber+1] == "*":
        return True, "next", endOfNumber + 1
    for index in range(startOfNumber, endOfNumber + 1):
        if previousLine[index] == "*" :
            return True, "previous", index
        if nextLine[index] == "*":
            return True, "next", index

    if startOfNumber > 0 and currentLine[startOfNumber-1] == "*":
        return True, "current", startOfNumber - 1
    if endOfNumber < len(currentLine) - 1 and currentLine[endOfNumber+1] == "*":
        return True, currentLine, endOfNumber + 1
    return False, "current", -1


def checkWhereNumberEnds(previousLine, startingIndex):
    endingIndex = startingIndex
    while endingIndex < len(previousLine) and previousLine[endingIndex].isnumeric():
        endingIndex += 1
    print(previousLine[startingIndex:endingIndex])
    return endingIndex - 1

def checkWhereNumberStarts(previousLine, endingIndex):
    startingIndex = endingIndex
    while startingIndex >= 0 and previousLine[startingIndex].isnumeric():
        startingIndex -= 1
    return startingIndex + 1

def adjacentStarHas2PartNumbers(previousLine, currentLine, nextLine, indexOfStar):
    numberOfPartNumbers = 0
    numbers = {}
    if indexOfStar > 0 and previousLine[indexOfStar-1].isnumeric():
        endingIndex = checkWhereNumberEnds(previousLine, indexOfStar-1)
        startingIndex = checkWhereNumberStarts(previousLine, endingIndex)
        numbers[(startingIndex, endingIndex+1)] = previousLine[startingIndex:endingIndex+1]

    if indexOfStar < len(currentLine) - 1 and previousLine[indexOfStar+1].isnumeric():
        startingIndex = checkWhereNumberStarts(previousLine, indexOfStar+1)
        endingIndex = checkWhereNumberEnds(previousLine, startingIndex)
        numbers[(startingIndex, endingIndex)] = previousLine[startingIndex:endingIndex+1]

    if indexOfStar > 0 and nextLine[indexOfStar-1].isnumeric():
        endingIndex = checkWhereNumberEnds(nextLine, indexOfStar - 1)
        startingIndex = checkWhereNumberStarts(nextLine, endingIndex)
        numbers[(startingIndex, endingIndex)] = nextLine[startingIndex:endingIndex+1]

    if indexOfStar < len(currentLine) - 1 and nextLine[indexOfStar+1].isnumeric():
        startingIndex = checkWhereNumberStarts(nextLine, indexOfStar+1)
        endingIndex = checkWhereNumberEnds(nextLine, startingIndex)
        numbers[(startingIndex, endingIndex)] = nextLine[startingIndex:endingIndex+1]

    if previousLine[indexOfStar].isnumeric():
        startingIndex = checkWhereNumberStarts(previousLine, indexOfStar)
        endingIndex = checkWhereNumberEnds(previousLine, startingIndex)
        numbers[(startingIndex, endingIndex)] = previousLine[startingIndex:endingIndex+1]

    if nextLine[indexOfStar].isnumeric():
        startingIndex = checkWhereNumberStarts(nextLine, indexOfStar)
        endingIndex = checkWhereNumberEnds(nextLine, startingIndex)
        numbers[(startingIndex, endingIndex)] = nextLine[startingIndex:endingIndex+1]

    if indexOfStar > 0 and currentLine[indexOfStar-1].isnumeric():
        endingIndex = indexOfStar - 1
        startingIndex = checkWhereNumberStarts(currentLine, endingIndex)
        numbers[(startingIndex, endingIndex)] = currentLine[startingIndex:endingIndex+1]

    if indexOfStar < len(currentLine) - 1 and currentLine[indexOfStar+1].isnumeric():
        startingIndex = indexOfStar + 1
        endingIndex = checkWhereNumberEnds(currentLine, startingIndex)
        numbers[(startingIndex, endingIndex)] = currentLine[startingIndex:endingIndex+1]

    print(numbers)
    numbersList = []
    for key in numbers.keys():
        numbersList.append(numbers[key])
    if len(numbers) == 2:
        print(f"Found 2 part numbers: {numbersList}")
        firstNumber = int(numbersList[0])
        secondNumber = int(numbersList[1])
        product = int(firstNumber) * int(secondNumber)
    else:
        product = int(numbersList[0])
        firstNumber = 0
        secondNumber = 0
    return len(numbers) == 2, product, (firstNumber, secondNumber)

def checkForNumbersWithAdjacentSymbols(currentLine, previousLine, nextLine, exPreviousLine, nextNextLine, previousLineStars, currentLineStars, nextLineStars):
    startOfNumber = -1
    endOfNumber = -1
    productOfPartElements = 0
    numbersAdded = []

    for index in range(0, len(currentLine)):
        if currentLine[index].isnumeric():
            if startOfNumber == -1:
                startOfNumber = index
        else:
            if startOfNumber != -1:
                endOfNumber = index - 1
                hasAdjacentStar, lineOnWhichTheStarIs, indexOfStar = checkForAdjacentStar(currentLine, previousLine, nextLine, startOfNumber, endOfNumber)
                if hasAdjacentStar:
                    print(f"Found adjacent star\nLine: {currentLine}")
                    if lineOnWhichTheStarIs == "previous":
                        print(f"Previous line has star: {previousLine}")
                        has2PartNumbers, product, numbers = adjacentStarHas2PartNumbers(exPreviousLine, previousLine, currentLine, indexOfStar)
                        if has2PartNumbers and indexOfStar not in previousLineStars:
                            productOfPartElements += product
                            previousLineStars.append(indexOfStar)
                    elif lineOnWhichTheStarIs == "next":
                        print(f"Next line has star: {nextLine}")
                        has2PartNumbers, product, numbers = adjacentStarHas2PartNumbers(currentLine, nextLine, nextNextLine, indexOfStar)
                        if has2PartNumbers and indexOfStar not in nextLineStars:
                            productOfPartElements += product
                            nextLineStars.append(indexOfStar)
                    elif lineOnWhichTheStarIs == "current":
                        print(f"Current line has star: {currentLine}")
                        has2PartNumbers, product, numbers = adjacentStarHas2PartNumbers(previousLine, currentLine, nextLine, indexOfStar)
                        if has2PartNumbers and indexOfStar not in currentLineStars:
                            productOfPartElements += product
                            currentLineStars.append(indexOfStar)
                startOfNumber = -1
                endOfNumber = -1
    return productOfPartElements

def parseLines(lines):
    sumOfPartElements = 0
    exPreviousLine = len(lines[0]) * "."
    previousLine = len(lines[0]) * "."
    previousLineStars = []
    currentLineStars = []
    nextLineStars = []
    for lineIndex in range(0, len(lines)):
        currentLine = lines[lineIndex]
        if lineIndex < len(lines) - 1:
            nextLine = lines[lineIndex + 1]
        else:
            nextLine = len(lines[0]) * "."
        if lineIndex < len(lines) - 2:
            nextNextLine = lines[lineIndex + 2]
        else:
            nextNextLine = len(lines[0]) * "."

        sumOfPartElements += checkForNumbersWithAdjacentSymbols(currentLine, previousLine, nextLine, exPreviousLine, nextNextLine, previousLineStars, currentLineStars, nextLineStars)
        exPreviousLine = previousLine
        previousLine = currentLine
        previousLineStars = currentLineStars
        currentLineStars = nextLineStars
        nextLineStars = []
    print(sumOfPartElements)



def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines[-1] += "\n"
        parseLines(lines)


main()
