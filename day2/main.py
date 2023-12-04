
def getNumberOfCubesOutOfASet(gameText: str, numberOfCubes: dict):
    gameSteps = gameText.split(" ")
    for stepIndex in range(0, len(gameSteps)):
        if gameSteps[stepIndex].isnumeric():
            if gameSteps[stepIndex+1][-1] == "," or gameSteps[stepIndex+1][-1] == ";" or gameSteps[stepIndex+1][-1] == "\n":
                gameSteps[stepIndex+1] = gameSteps[stepIndex+1][:-1]
            numberOfCubes[gameSteps[stepIndex+1]] += int(gameSteps[stepIndex])
    return numberOfCubes

def checkIfNewMaximumNumberOfCubes(maximumNumberOfCubes, currentNumberOfCubes):
    if maximumNumberOfCubes["red"] < currentNumberOfCubes["red"]:
        maximumNumberOfCubes["red"] = currentNumberOfCubes["red"]
    if maximumNumberOfCubes["green"] < currentNumberOfCubes["green"]:
        maximumNumberOfCubes["green"] = currentNumberOfCubes["green"]
    if maximumNumberOfCubes["blue"] < currentNumberOfCubes["blue"]:
        maximumNumberOfCubes["blue"] = currentNumberOfCubes["blue"]
    return maximumNumberOfCubes

def parseLines(lines):
    sumOfIndexes = 0
    sumOfPowers = 0
    for line in lines:
        gameNumber, gameText = line[5:].split(":")
        setsInGame = gameText.split(";")
        gameIsOk = True
        maximumNumberOfCubes = {"red": 0, "green": 0, "blue": 0}
        for currentSet in setsInGame:
            numberOfCubes = {"red": 0, "green": 0, "blue": 0}
            numberOfCubes = getNumberOfCubesOutOfASet(currentSet, numberOfCubes)
            maximumNumberOfCubes = checkIfNewMaximumNumberOfCubes(maximumNumberOfCubes, numberOfCubes)
            if numberOfCubes["red"] > 12 or numberOfCubes["green"] > 13 or numberOfCubes["blue"] > 14:
                gameIsOk = False
        powerOfGame = maximumNumberOfCubes["red"] * maximumNumberOfCubes["green"] * maximumNumberOfCubes["blue"]
        sumOfPowers += powerOfGame
        if gameIsOk:
            sumOfIndexes += int(gameNumber)
    print(f"First part: {sumOfIndexes}")
    print(f"Second part: {sumOfPowers}")

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)

main()