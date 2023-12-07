import re

seeds = []
seedToSoil = {}
soilToFertilizer = {}
fertilizerToWater = {}
waterToLight = {}
lightToTemperature = {}
temperatureToHumidity = {}
humidityToLocation = {}
minLocation = 10000000000000000


def countMap(mapName, line):
    coordinates = re.split(r'\s+', line)
    print(coordinates)
    if coordinates[0] == "":
        coordinates = coordinates[1:]
    lengthOfCoordinates = int(coordinates[2])
    destinationStart = int(coordinates[0])
    sourceStart = int(coordinates[1])
    if mapName == "seedToSoil":
        seedToSoil[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)
    elif mapName == "soilToFertilizer":
        soilToFertilizer[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)
    elif mapName == "fertilizerToWater":
        fertilizerToWater[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)
    elif mapName == "waterToLight":
        waterToLight[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)
    elif mapName == "lightToTemperature":
        lightToTemperature[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)
    elif mapName == "temperatureToHumidity":
        temperatureToHumidity[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)
    elif mapName == "humidityToLocation":
        humidityToLocation[(sourceStart, sourceStart + lengthOfCoordinates)] = (destinationStart, destinationStart + lengthOfCoordinates)


def addSeedLocationsData(lines):
    numbers = 0
    lineLength = len(lines)
    currentLine = 0
    while currentLine < lineLength:
        line = lines[currentLine]
        if line.startswith("seeds:"):
            seedsList = re.split(r'\s+', line[6:])
            for seed in seedsList:
                if seed != "":
                    seeds.append(int(seed))
            print(seeds)
        elif line.startswith("seed-to-soil"):
            currentLine += 1
            line = lines[currentLine]
            while line != "\n":
                countMap("seedToSoil", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]

        elif line.startswith("soil-to-fertilizer"):
            currentLine += 1
            line = lines[currentLine]
            while line != "\n":
                countMap("soilToFertilizer", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]
        elif line.startswith("fertilizer-to-water"):
            currentLine += 1
            line = lines[currentLine]
            while line != "\n":
                countMap("fertilizerToWater", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]
        elif line.startswith("water-to-light"):
            currentLine += 1
            line = lines[currentLine]
            while line != "\n":
                countMap("waterToLight", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]
        elif line.startswith("light-to-temperature"):
            currentLine += 1
            line = lines[currentLine]
            while line != "\n":
                countMap("lightToTemperature", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]
        elif line.startswith("temperature-to-humidity"):
            currentLine += 1
            line = lines[currentLine]
            while line != "\n":
                countMap("temperatureToHumidity", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]
        elif line.startswith("humidity-to-location"):
            currentLine += 1
            line = lines[currentLine]
            while currentLine < lineLength:
                line = lines[currentLine]
                countMap("humidityToLocation", line)
                currentLine += 1
                if currentLine < lineLength:
                    line = lines[currentLine]
        currentLine += 1

def checkIfMinimumLocation(value):
    global minLocation
    if value < minLocation:
        minLocation = value

def manageSeeds():
    for seed in seeds:
        print(f"SEED {seed}")
        soil = -1
        for seedRange in seedToSoil:
            if seedRange[0] <= seed <= seedRange[1]:
                soil = seed - seedRange[0] + seedToSoil[seedRange][0]
        if soil == -1:
            soil = seed
        print(f"has soil {soil}")
        fertilizer = -1
        for soils in soilToFertilizer:
            if soils[0] <= soil <= soils[1]:
                fertilizer = soil - soils[0] + soilToFertilizer[soils][0]
        if fertilizer == -1:
            fertilizer = soil
        print(f"has fertilizer {fertilizer}")
        water = -1
        for fertilizers in fertilizerToWater:
            if fertilizers[0] <= fertilizer <= fertilizers[1]:
                water = fertilizer - fertilizers[0] + fertilizerToWater[fertilizers][0]
        if water == -1:
            water = fertilizer
        print(f"has water {water}")
        light = -1
        for waters in waterToLight:
            if waters[0] <= water <= waters[1]:
                light = water - waters[0] + waterToLight[waters][0]
        if light == -1:
            light = water
        print(f"has light {light}")
        temperature = -1
        for lights in lightToTemperature:
            if lights[0] <= light <= lights[1]:
                temperature = light - lights[0] + lightToTemperature[lights][0]
        if temperature == -1:
            temperature = light
        print(f"has temperature {temperature}")

        humidity = -1
        for temperatures in temperatureToHumidity:
            if temperatures[0] <= temperature <= temperatures[1]:
                humidity = temperature - temperatures[0] + temperatureToHumidity[temperatures][0]
        if humidity == -1:
            humidity = temperature
        print(f"has humidity {humidity}")
        location = -1
        for humidities in humidityToLocation:
            if humidities[0] <= humidity <= humidities[1]:
                location = humidity - humidities[0] + humidityToLocation[humidities][0]
        if location == -1:
            location = humidity
        print(f"has location {location}")
        checkIfMinimumLocation(location)

def printLocation():
    print(minLocation)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        addSeedLocationsData(lines)
        manageSeeds()
        printLocation()

main()
