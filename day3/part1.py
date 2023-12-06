
def checkForAdjacentSymbols(currentLine, previousLine, nextLine, startOfNumber, endOfNumber):

    if ((startOfNumber > 0 and not previousLine[startOfNumber-1].isnumeric() and previousLine[startOfNumber-1] != "." and previousLine[startOfNumber-1] != "\n") or
            (endOfNumber < len(currentLine) - 1 and not previousLine[endOfNumber+1].isnumeric() and previousLine[endOfNumber+1] != "." and previousLine[endOfNumber+1] != "\n")):
        return True
    if ((startOfNumber > 0 and not nextLine[startOfNumber-1].isnumeric() and nextLine[startOfNumber-1] != "." and nextLine[startOfNumber-1] != "\n") or
            (endOfNumber < len(currentLine) - 1 and not nextLine[endOfNumber+1].isnumeric() and nextLine[endOfNumber+1] != "." and nextLine[endOfNumber+1] != "\n")):
        return True
    for index in range(startOfNumber, endOfNumber + 1):
        if (not previousLine[index].isnumeric() and previousLine[index] != ".") or (not nextLine[index].isnumeric() and nextLine[index] != "."):
            return True
    if startOfNumber > 0 and not currentLine[startOfNumber-1].isnumeric() and currentLine[startOfNumber-1] != "." and currentLine[startOfNumber-1] != "\n":
        return True
    if endOfNumber < len(currentLine) - 1 and not currentLine[endOfNumber+1].isnumeric() and currentLine[endOfNumber+1] != "." and currentLine[endOfNumber+1] != "\n":
        return True
    return False

def checkForNumbersWithAdjacentSymbols(currentLine, previousLine, nextLine):
    startOfNumber = -1
    endOfNumber = -1
    sumOfPartElements = 0

    for index in range(0, len(currentLine)):
        if currentLine[index].isnumeric():
            if startOfNumber == -1:
                startOfNumber = index
        else:
            if startOfNumber != -1:
                endOfNumber = index - 1
                if checkForAdjacentSymbols(currentLine, previousLine, nextLine, startOfNumber, endOfNumber):
                    sumOfPartElements += int(currentLine[startOfNumber:endOfNumber + 1])
                startOfNumber = -1
                endOfNumber = -1
    return sumOfPartElements

def parseLines(lines):
    sumOfPartElements = 0
    previousLine = len(lines[0]) * "."
    for lineIndex in range(0, len(lines)):
        currentLine = lines[lineIndex]
        if lineIndex < len(lines) - 1:
            nextLine = lines[lineIndex + 1]
        else:
            nextLine = len(lines[0]) * "."

        sumOfPartElements += checkForNumbersWithAdjacentSymbols(currentLine, previousLine, nextLine)
        previousLine = currentLine
    print(sumOfPartElements)



def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines[-1] += "\n"
        parseLines(lines)

main()
