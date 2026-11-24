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
            for word in row.split():
                #Fixar så att ordet inte kan bestå av citat tecken, punkt och komma
                translator = str.maketrans('', '', string.punctuation)
                fixedWord = word.translate(translator)
                if fixedWord.isalpha():
                    hashTableSize += 1
                    wordQueue.enqueue(fixedWord)
    return wordQueue, hashTableSize


def createWordNode(word, words):
    try:
        wordNode = words.search(word)
        wordNode.amount += 1
    except KeyError:
        words.store(word, Word(word))

def createWordPairNode(word, nextWord, wordPairs):
    try:
        wordPairNode = wordPairs.search(word + nextWord)
        wordPairNode.amount += 1
    except KeyError:
        wordPairs.store(word+nextWord, WordPair(word, nextWord))
        wordPairNode = wordPairs.search(word+nextWord)

def createWordTables(wordQueue, hashTableSize):
    words = Hashtable(hashTableSize)
    wordPairs = Hashtable(hashTableSize)
    wordPairsLinkedQ = LinkedQ()

    while wordQueue.isEmpty() == False:
        word = wordQueue.dequeue().value
        try:
            createWordNode(word, words)
        except:
            continue

        #Kollar om peek ens går, annars finns inte ett till ord och därför ordpar med just den.
        if wordQueue.peek() == False:
            break
            
        createWordPairNode(word, wordQueue.peek(), wordPairs)

    return words
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
    words = createWordTables(wordQueue, int(hashTableSize))
    print(words)


main()