import string
from linkedQFile import LinkedQ
from hashtable import Hashtable
from word import Word
from wordPair import WordPair
from maxHeap import MaxHeap

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
        
    def __str__(self):
        return self.word
    
def getWordQueue():
    wordQueue = LinkedQ()
    hashTableSize = 0
    with open("acd_alla.txt", encoding="utf-8") as storiesText:
        for row in storiesText:
            for word in row.strip().split():
                #Fixar så att ordet inte kan bestå av citat tecken, punkt och komma
                translator = str.maketrans('', '', string.punctuation)
                fixedWord = word.translate(translator)
                if fixedWord.isalpha():
                    hashTableSize += 1
                    wordQueue.enqueue(fixedWord)
    return wordQueue, hashTableSize


def createWordNode(word, words):
    try:
        wordNode = words.search(word.lower())
        wordNode.amount += 1
    except KeyError:
        words.store(word.lower(), Word(word.lower()))

def createWordPairNode(word, nextWord, wordPairs, hashTableKeys):
    try:
        wordPairNode = wordPairs.search((word + nextWord).lower())
        wordPairNode.amount += 1
    except KeyError:
        wordPairs.store((word+nextWord).lower(), WordPair(word.lower(), nextWord.lower()))
        wordPairNode = wordPairs.search((word+nextWord).lower())
        hashTableKeys.enqueue(word + nextWord)

#Creates all wordPairs and words
def createWordTables(wordQueue, hashTableSize):
    words = Hashtable(hashTableSize)
    wordPairs = Hashtable(hashTableSize)
    hashTableKeys = LinkedQ()

    while wordQueue.isEmpty() == False:
        word = wordQueue.dequeue()
        #If error is thrown that means that a word doesn't already exist meaning the wordpair shouldn't exists
        #Therefor we go to next itteration of the loop with continue
        try:
            createWordNode(word, words)
        except:
            continue

        #Kollar om peek ens går, annars finns inte ett till ord och därför ordpar med just den.
        if wordQueue.peek() == False:
            break
            
        createWordPairNode(word, wordQueue.peek(), wordPairs, hashTableKeys)
    return words, wordPairs, hashTableKeys

#Calculates the possibility for a word to be followed by another word in the text
def calculateWordPairChance(words, wordPairs, hashTableKeys):
    while hashTableKeys.isEmpty() == False:
        wordPairsKey = hashTableKeys.dequeue()
        wordPair = wordPairs.search(wordPairsKey.lower())
        if wordPair.amount > 1:
            word = words.search(wordPair.firstWord)
            wordPair.setChance(word.amount)

"""
def beemSearch(firstWord):
    q.enqueue(firstWord)
    while not q.isEmpty():
        node = q.dequeue()
        makeChildrenSuccess, lastNode = makeChildren(node, userInput[1].strip(), wordList, oldList, q)
        if makeChildrenSuccess == False:
            break

def makeChildren(startNode, endWord, wordList, oldList, q):
    startWord = startNode.word

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","å","ä","ö"]
    for i in range(len(startWord)):
        for char in alphabet:

            tempWord = startWord.replace(startWord[i], char)
            tempNode = ParentNode(tempWord, startNode)
            if tempWord == endWord and tempWord in wordList:
                #print(f"Det finns en väg mellan orden {tempWord} och {endWord}")
                oldList.put(tempWord)
                return False, tempNode
            
            if tempWord in wordList and tempWord != startWord:

                if (tempWord in oldList) == False: 
                    q.enqueue(tempNode)
                    oldList.put(tempWord)
        i += 1
    return True, None
"""

def main():
    #q = LinkedQ()
    #firstWord = ParentNode()
    wordQueue, hashTableSize = getWordQueue()
    words, wordPairs, hashTableKeys = createWordTables(wordQueue, int(hashTableSize))
    calculateWordPairChance(words, wordPairs, hashTableKeys)


main()