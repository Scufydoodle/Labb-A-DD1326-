class WordPair():
    def __init__ (self, firstWord, secondWord):
        self.firstWord = firstWord
        self.secondWord = secondWord
        self.amount = 0

    def __str__(self):
        return f"Ordpar: {self.firstWord}, {self.secondWord} Mängd: {self.amount}"