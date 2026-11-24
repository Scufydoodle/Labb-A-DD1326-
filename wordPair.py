class WordPair():
    def __init__ (self, firstWord, secondWord):
        self.firstWord = firstWord
        self.secondWord = secondWord
        self.amount = 1
        self.chance = None

    def __str__(self):
        return f"Ordpar: {self.firstWord}, {self.secondWord} Mängd: {self.amount}"

    #Calculates the chance of the word pair being in the text
    def setChance(self, firstWordAmount):
        self.chance = self.amount / firstWordAmount