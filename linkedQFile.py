class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.data = []

    #Prints the whole linked-list queue
    def __str__(self):
        textOutput = ""

        node = self.__first
        # if node == None: check for isEmpty()
        #     print("Empty")

        if node.next == None:
            return node.value

        while node.next != None:
            textOutput += f"{node.value}\n"
            node = node.next
        return textOutput
    
    #Creates a new node based on sent in value and adds it to the queue
    def enqueue(self, value):
        node = Node(value)

        #if queue is empty the new node becomes the first and last node in the queue
        if self.isEmpty():
            self.__first = node
            self.__last = node
            return
        #else the current last node gets a next node (the new node)  and the new last node is the new node    
        self.__last.next = node
        self.__last = node
    #Removes the first element in queue and returns it
    def dequeue(self):
        #current second node in the queue
        returnValue = self.__first
        #new first nodes is the old second node in queue
        self.__first = self.__first.next
        return returnValue
    #Checks if the queue is empty
    def isEmpty(self):
        if self.__first == None:
            return True
        return False
    
    #Turns all the items in the list into nodes and add them to the queue
    def queueLinkedQ(self, list):
        for element in list:
            self.enqueue(element)

    #Gets the first element in the linkedQ without removing it
    def peek(self):
        try:
            return self.__first.value
        except:
            return False