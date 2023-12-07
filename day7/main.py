import re


class card:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = bet
        self.cards = {}
        self.type = "three of a kind"
        self.countCards()
        self.importanceOfTypes = {
            "five of a kind": 10,
            "four of a kind": 9,
            "full house": 8,
            "three of a kind": 7,
            "two pairs": 6,
            "one pair": 5,
            "high card": 4
        }
        self.importanceOfCards = {
            "A": "Z",
            "K": "Y",
            "Q": "X",
            "J": "W",
            "T": "V",
            "9": "U",
            "8": "T",
            "7": "S",
            "6": "R",
            "5": "Q",
            "4": "P",
            "3": "O",
            "2": "N"
        }
        self.handByImportance = self.parseImportanceOfHand()

    def parseImportanceOfHand(self):
        importance = ""
        for character in self.hand:
            importance += self.importanceOfCards[character]
        return importance

    def countCards(self):
        for card in self.hand:
            if card in self.cards:
                self.cards[card] += 1
            else:
                self.cards[card] = 1
        pairs = []
        for card in self.cards:
            if self.cards[card] != 0:
                pairs.append(self.cards[card])
        if len(pairs) == 1:
            self.type = "five of a kind"
        elif len(pairs) == 2:
            if 3 in pairs:
                self.type = "full house"
            elif 4 in pairs:
                self.type = "four of a kind"
            else:
                self.type = "two pairs"
        elif len(pairs) == 3:
            if 3 in pairs:
                self.type = "three of a kind"
            elif pairs[0] == 1 and pairs[1] == 1:
                self.type = "one pair"
            else:
                self.type = "two pairs"
        elif len(pairs) == 4:
            if 2 in pairs:
                self.type = "one pair"
            else:
                self.type = "high card"
        else:
            self.type = "high card"

    def __eq__(self, other):
        return self.hand == other.hand

    def __gt__(self, other):
        if self.type == other.type:
            return self.handByImportance > other.handByImportance
        else:
            return self.importanceOfTypes[self.type] > other.importanceOfTypes[other.type]

    def __lt__(self, other):
        if self.type == other.type:
            return self.handByImportance < other.handByImportance
        else:
            return self.importanceOfTypes[self.type] < other.importanceOfTypes[other.type]

    def __ge__(self, other):
        if self.type == other.type:
            return self.handByImportance >= other.handByImportance
        else:
            return self.importanceOfTypes[self.type] >= other.importanceOfTypes[other.type]

    def __le__(self, other):
        if self.type == other.type:
            return self.handByImportance <= other.handByImportance
        else:
            return self.importanceOfTypes[self.type] <= other.importanceOfTypes[other.type]

    def __str__(self):
        return self.hand + " " + str(self.bet) + " " + self.type







def parseLines(lines):
    handsList = []
    for line in lines:
        lineArgs = re.split(r'\s+', line)
        if lineArgs[0] == "":
            lineArgs = lineArgs[1:]
        hand = lineArgs[0]
        bet = int(lineArgs[1])
        c = card(hand, bet)
        handsList.append(c)
    handsList.sort()
    bidSum = 0
    # for hand in handsList:
    #     print(hand)
    for handIndex in range(0, len(handsList)):
        bidSum += handsList[handIndex].bet * (handIndex + 1)
    print(bidSum)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        parseLines(lines)

main()

