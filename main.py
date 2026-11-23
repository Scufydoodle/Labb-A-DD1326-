from linkedQFile import Node, LinkedQ

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
        
    def __str__(self):
        return self.word

def getWordQueue():
    wordQueue = LinkedQ()
    with open("acd_alla.txt", encoding="utf-8") as storiesText:
        for row in storiesText:
            for word in row.split():
                wordQueue.enqueue(word)

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
    getWordQueue()

main()