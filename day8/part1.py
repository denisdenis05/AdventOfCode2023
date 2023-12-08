import re

directions = []
elementsToIterateThrough = {}

def inputDirections(line):
    for character in line:
        if character == "L":
            directions.append(0)
        elif character == "R":
            directions.append(1)


def inputElements(lines):
    for line in lines:
        lineArgs = line.split("=")
        futureTuple = []
        element = re.split(r'\s+', lineArgs[0])
        for el in element:
            if el != "":
                element = el
                break
        tuple = re.split(r'\s+', lineArgs[1])
        for tp in tuple:
            if tp != "":
                futureTuple.append(tp)
        element1 = (futureTuple[0].replace("(", "")).replace(",", "")
        element2 = (futureTuple[1].replace(")", "")).replace(",", "")
        elementsToIterateThrough[element] = (element1, element2)



def parseLines(lines):
    handsList = []
    inputDirections(lines[0])
    lines = lines[2:]
    inputElements(lines)

def goThroughElementsTillZZZ():
    key = "AAA"
    position = 0
    steps = 1
    while(True):
        leftOrRight = directions[position]
        if elementsToIterateThrough[key][leftOrRight] == "ZZZ":
            print(steps)
            return
        position += 1
        key = elementsToIterateThrough[key][leftOrRight]
        steps += 1
        if position == len(directions):
            position = 0



def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)
        goThroughElementsTillZZZ()


main()
