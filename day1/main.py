from digitspelling import digitspelling

def updateFirstAndLastDifit(firstDigit, lastDigit, valueToAdd):
    if firstDigit == -1:
        firstDigit = valueToAdd
    else:
        lastDigit = valueToAdd
    return firstDigit, lastDigit

def getFirstAndLastDigit(text: str):
    firstDigit = -1
    lastDigit = -1
    for characterIndex in range(0, len(text)):
        if text[characterIndex].isdigit():
            firstDigit, lastDigit = updateFirstAndLastDifit(firstDigit, lastDigit, int(text[characterIndex]))
        else:
            for digit in digitspelling:
                if text[characterIndex:].startswith(digitspelling[digit]):
                    firstDigit, lastDigit = updateFirstAndLastDifit(firstDigit, lastDigit, digit)


    if firstDigit == -1:
        return 0, 0
    if lastDigit == -1:
        return firstDigit, firstDigit
    return firstDigit, lastDigit


def parseLines(lines):
    sum = 0
    for line in lines:
        firstDigit, lastDigit = getFirstAndLastDigit(line)
        sum += firstDigit*10+lastDigit
    print(sum)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)

main()