import re

times = ""
distances = ""

def parseLines(lines):
    global times
    global distances
    numbers = 0
    for line in lines:
        if line.startswith("Time:"):
            distanceText = re.split(r'\s+', line[5:])
            for distance in distanceText:
                if distance != "":
                    times += distance
        elif line.startswith("Distance:"):
            distanceText = re.split(r'\s+', line[9:])
            for distance in distanceText:
                if distance != "":
                    distances += distance
    times = int(times)
    distances = int(distances)


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)
        margin = 1
        numberOfPossibleWinnngOutcomes = 0
        for timePressed in range(1, times):
            if ((-1) * (timePressed * timePressed) + timePressed * times) > distances:
                numberOfPossibleWinnngOutcomes += 1
        margin *= numberOfPossibleWinnngOutcomes
    print(margin)
main()
