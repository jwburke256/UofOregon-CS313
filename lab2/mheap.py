class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.
    ...


    Attributes
    ----------
    max_size: int
        maximum size of the heap
    length : int
        Current length of the heap based on amount of data
    heap : list
        Data that resides in the heap given as a list

    Methods
    -------
    get_heap():
        Returns the data residing in the heap as a list
    insert(data):
        Inserts an element into the heap.
        Raises IndexError if the heap is full.
    peek():
        Returns the maximum value in the heap without removing it.
    extract_max():
        Removes and returns the maximum value in the heap.
        Raises KeyError if the heap is empty.
    __heapify(curr_index, list_length=None):
        Given a current index and length of the list, checks
        the children nodes to verify if the current node is bigger.
        If not it swaps the parent with the largest child, and then
        recursively calls on the child. This helps maintain the property of
        the max_heap
    build_heap():
        builds a max heap from the current heap which is an unordered
        list.
    __get_parent(loc):
        gets the parent node index when given the current child node index
    __get_left(loc):
        gets the left child node index when given a parent node index
    __get_right(loc):
        gets the right child node index when given a parent node index
    __swap(a, b):
        swap elements located at given indexes a and b of the heap
    """


    def __init__(self, size=20, data=None):
        """Initialize a binary max-heap.

        Parameters
        ----------
        size : int
            Total capacity of the heap.
        data : list
            List containing the desired heap contents.
            The list is used in-place, not copied, so its contents
            will be modified by heap operations.
            If data is specified, then the size field is ignored.
        """

        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size

    def get_heap(self):
        """Returns the data residing in the heap as a list"""
        return self.heap

    def insert(self, data):
        """Inserts an element into the heap.
        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        try:
            if self.length == self.max_size:
                raise IndexError
        except IndexError:
            print("Heap is full")
            raise IndexError
        self.length += 1
        self.heap[self.length - 1] = data
        index = (self.length - 1)
        parent = self.__get_parent(index)
        if index == 0:
            return
        while (self.heap[index] > self.heap[parent]) and (
                self.heap[parent] is not None):
            self.__swap(index, parent)
            index = parent
            if index == 0:
                break
            parent = self.__get_parent(index)


    def peek(self):
        """Returns the maximum value in the heap without removing it."""
        if self.length == 0:
            return None
        else:
            return self.heap[0]

    def extract_max(self):
        """Removes and returns the maximum value in the heap.
        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        try:
            if self.length == 0:
                raise KeyError
        except KeyError:
            print("Heap is empty")
            raise KeyError

        maxVal = self.heap[0]
        self.__swap(0, (self.length - 1))
        self.heap[self.length-1] = None
        self.length -= 1
        self.__heapify(0, self.length)
        return maxVal

    def __heapify(self, curr_index, list_length=None):
        """Given a current index and length of the list, checks
        the children nodes to verify if the current node is bigger.
        If not it swaps the parent with the largest child, and then
        recursively calls on the child. This helps maintain the property of
        the max_heap"""
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        l = self.__get_left(curr_index)
        r = self.__get_right(curr_index)
        largest = curr_index
        if l <= list_length-1:
            if self.heap[l] > self.heap[largest]:
                largest = l
        if r <= list_length-1:
            if self.heap[r] > self.heap[largest]:
                largest = r
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, list_length)

    def build_heap(self):
        """builds a max heap from the current heap which is an unordered
        list."""
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        for i in range(((self.length-1) // 2), -1, -1):
            self.__heapify(i, self.length)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        """gets the parent node index when given the current child node index"""
        # left child has odd location index
        # right child has even location index
        if loc % 2 == 0:
            parent = int((loc - 2) / 2)
        else:
            parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        """gets the left child node index when given a parent node index"""
        return 2 * loc + 1

    def __get_right(self, loc):
        """gets the right child node index when given a parent node index"""
        return 2 * loc + 2

    def __swap(self, a, b):
        """swap elements located at given indexes a and b of the heap"""
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """Sorts a given list in place using heapsort then returns the sorted
    list in ascending order."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
    heap = max_heap((len(l)), l)
    heap.build_heap()
    print(heap.get_heap())
    for i in range(len(l)-1, -1, -1):
        l[i] = heap.extract_max()
    return l
