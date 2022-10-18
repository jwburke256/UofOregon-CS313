class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """

    def __init__(self, data=None, next_node=None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node


class Queue(object):
    """
    A class to represent a queue.

    ...

    Attributes
    ----------
    head : Node
        The current head node at the front of the queue
    tail : Node
        The current tail node at the back of the queue

    Methods
    -------
    str():
        returns a string that contains the current data in the Queue
    enqueue():
        Adds a new node to the end of the Queue
    dequeue():
        Removes and returns the first Node currently in the Queue
    isEmpty():
        Returns true if Queue is empty, false if not
    """

    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        pass

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        newNode = Node(newData)
        if self.__head is None:
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.setNext = self.__tail
            self.__tail = newNode

    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty() is True:
            return None
        elif self.__head == self.__tail:
            result = self.__head.getData()
            self.__head = None
            self.__tail = None
            return result
        else:
            result = self.__tail
            prev = None
            while result.getNext() is not self.__head:
                prev = result
                result = result.getNext()




    def isEmpty(self):
        '''Check if the Queue is empty.'''
        pass


class Stack(object):
    """
    A class to represent a stack.

    ...

    Attributes
    ----------
    top : Node
        The node that currently is at the top of the stack

    Methods
    -------
    str():
        returns a string that contains the current data in the Stack
    push(newData):
        Adds a new node to the top of the stack
    pop():
        Removes and returns the last submitted Node from the top of the stack
    isEmpty():
        Returns true if stack is empty, false if not
    """

    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        node = self.__top
        strResult = '['
        while node.getNext() is not None:
            strResult = strResult + (str(node.getData()) + ', ')
            node = node.getNext()

        strResult = strResult + str(node.getData()) + ']'
        return strResult

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        newNode = Node(newData)
        if self.isEmpty():  # uses isEmpty to determine if initial node needs to be added
            self.__top = newNode
        else:
            newNode.setNext(self.__top)
            self.__top = newNode

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.isEmpty():
            return None
        else:
            popNode = self.__top
            self.__top = self.__top.getNext()
            return popNode.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        if self.__top is None:
            return True
        else:
            return False


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value
    return


def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return
