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
                if word.isalpha():
                    hashTableSize += 1
                    wordQueue.enqueue(word)
    return wordQueue, hashTableSize

def createWordPair(wordQueue):
    words = Hashtable()
    wordPairs = Hashtable()
    wordPairsLinkedQ = LinkedQ()
    while wordQueue.isEmpty() == False:
        word = wordQueue.dequeue().value
        nextWord = wordQueue.peek()
        if words.search(word) != None:
            wordNode = words.search(word)
            wordNode.amount += 1
        else:
            words.store(word, Word(word))
            continue

        if wordQueue.peek() != None:
            if wordPairs.search(word + nextWord) != None:
                wordPairNode = wordPairs.search(word + nextWord)
                wordPairNode.amount += 1
                wordPairsLinkedQ.enqueue(wordPairNode)
            else:
                wordPairs.store(word+nextWord, WordPair(word, nextWord))
    return words, wordPairs
            


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
    words, wordPairs = createWordPair(wordQueue, hashTableSize)

main()