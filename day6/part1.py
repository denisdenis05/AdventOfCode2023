import re

times = []
distances = []

def parseLines(lines):
    global times
    global distances
    numbers = 0
    for line in lines:
        if line.startswith("Time:"):
            distanceText = re.split(r'\s+', line[5:])
            for distance in distanceText:
                if distance != "":
                    times.append(int(distance))
        elif line.startswith("Distance:"):
            distanceText = re.split(r'\s+', line[9:])
            for distance in distanceText:
                if distance != "":
                    distances.append(int(distance))


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)
        margin = 1
        for race in range(0, len(times)):
            numberOfPossibleWinnngOutcomes = 0
            for timePressed in range(1, times[race]):
                if ((-1) * (timePressed * timePressed) + timePressed * times[race]) > distances[race]:
                    numberOfPossibleWinnngOutcomes += 1
            margin *= numberOfPossibleWinnngOutcomes
    print(margin)
main()
