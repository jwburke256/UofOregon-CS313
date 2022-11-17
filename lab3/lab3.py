class Node(object):
    """
    A class to represent a node in a binary search tree.

    ...

    Attributes
    ----------
    parent : object of class Node
        A pointer to the parent node of the current node in a binary search tree
    left : object of class Node
        A pointer to the left child node of the current node in a binary search
        tree
    right : object of class Node
        A pointer to the right child node of the current node in a binary
        search tree
    data : int
        An individual number to be stored in a node
    """
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """Binary Search Tree

        Supports most standard Binary Search Tree operations (insert, min,
        max, contains, find_successor, and contains).
        Can be used for storing integer data in a sorted order, and then able to
        be printed out in a specified manner with calling the desired traversal
        method (inorder, preorder, postorder). Tree has a maximum height of
        log n.
        ...


        Attributes
        ----------
        root: int
            first node in the Binary Search Tree

        Methods
        -------
        print():
            Prints out the data of all nodes in order
        __print(curr_node):
            Recursively prints a subtree (in order), rooted at curr_node
        insert(data):
            inserts data into the binary search tree by traversing the tree
            to one of the leaves and inserts as one of the previous null
            children to become the new leaf
        min():
            Returns the minimum value held in the tree.
            Returns None if the tree is empty
        max():
            Returns the maximum value held in the tree.
            Returns None if the tree is empty
        __find_node(data):
            Returns the node with that particular data value. If data not found
            it returns None instead.
        contains(data):
            Returns True if node containing data is present in the tree.
            Otherwise, function returns False.
        ____iter__():
            iterate over the nodes with inorder traversal using a for loop
        inorder():
            Used in conjunction with __traverse, returns the binary search
            tree values inorder
        preorder():
            Used in conjunction with __traverse, returns the binary search
            tree values preorder
        postorder():
            Used in conjunction with __traverse, returns the binary search
            tree values postorder
        __traverse(curr_node, traversal_type):
            helper method for traversal functions, implemented using generators
            to return the binary search tree values based on given
            traversal_type
        find_successor(data):
            Find the successor node in a given Binary Search Tree based off the
            data argument. If the value specified by find_successor does NOT
            exist in the tree, then the function raises a KeyError exception. If
            no successor exists for a given value that exists in the tree, then
            the function returns None
        __transplant(parent, child):
            Helper function for delete that moves a subtree of a deleted node
            into the correct position.
        delete(data):
            Find the node to delete. If the value specified by delete does NOT
            exist in the tree, then the function doesn't change the tree and
            instead raises a KeyError exception. If node found function utilizes
            transplant as needed to delete the node and adjust the tree.
        """


    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        """Prints out the data of all nodes in order"""
        self.__print(self.root)


    def __print(self, curr_node):
        """Recursively prints a subtree (in order), rooted at curr_node"""
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        """inserts data into the binary search tree by traversing the tree
        to one of the leaves and inserts as one of the previous null children
        to become the new leaf"""
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        node = Node(data)
        x = self.root
        y = None
        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        return


    def min(self):
        """Returns the minimum value held in the tree.
        Returns None if the tree is empty"""
        if self.root is None:
            return None
        else:
            x = self.root
            while x.left is not None:
                x = x.left
            return x.data

    def max(self):
        """Returns the maximum value held in the tree.
        Returns None if the tree is empty"""
        if self.root is None:
            return None
        else:
            x = self.root
            while x.right is not None:
                x = x.right
            return x.data

    def __find_node(self, data):
        """Returns the node with that particular data value. If data not found
        it returns None instead."""
        if self.root is None or data is None:
            return None
        node = self.root
        while node is not None:
            if data == node.data:
                return node
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def contains(self, data):
        """Returns True if node containing data is present in the tree.
        Otherwise, function returns False."""
        # you may use a helper method __find_node() to find a particular node
        # with the data value and return that node
        found = self.__find_node(data)
        if found is None:
            return False
        else:
            return True

    def __iter__(self):
        """iterate over the nodes with inorder traversal using a for loop"""
        return self.inorder()

    def inorder(self):
        """Used in conjunction with __traverse, returns the binary search
        tree values inorder"""
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, 1)

    def preorder(self):
        """Used in conjunction with __traverse, returns the binary search
        tree values preorder"""
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, 2)

    def postorder(self):
        """Used in conjunction with __traverse, returns the binary search
        tree values postorder"""
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, 3)

    def __traverse(self, curr_node, traversal_type):
        """helper method for traversal functions, implemented using generators
        to return the binary search tree values based on given traversal_type"""
        # all the traversals can be implemented using a single method

        #Yield data of the correct node/s
        if curr_node is not None:
            if traversal_type == 1:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == 2:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == 3:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data
        else:
            return None

    def find_successor(self, data):
        """Find the successor node in a given Binary Search Tree based off the
        data argument. If the value specified by find_successor does NOT
        exist in the tree, then the function raises a KeyError exception. If
        no successor exists for a given value that exists in the tree, then
        the function returns None"""
        # helper method to implement the delete method but may be called on its
        # own. If the right subtree of the node is nonempty,then the
        # successor is just the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until
        # a node that is the left child of its parent is encountered. The
        # parent of the found node will be the successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        node = self.__find_node(data)
        try:
            if node is None:
                raise KeyError
        except KeyError:
            print("Given node does not exist in current Binary Search Tree")
            raise KeyError
        # Check to see if node is last from in order walk
        if node.data == self.max():
            return None
        # Right subtree not empty, successor is leftmost node in right subtree or right node itself
        if node.right is not None:
            node = node.right
            while node is not None:
                prevNode = node
                node = node.left
            return prevNode
        # Right subtree empty, find lowest ancestor of parent that will be successor
        elif node.right is None:
            try:
                if node.parent is None:
                    raise KeyError
            except KeyError:
                print("Successor does not exist in current Binary Search Tree")
                raise KeyError
            y = node.parent
            while ((y is not None) and (node == y.right)):
                node = y
                y = y.parent
            return y
        else:
            return None

    def __transplant(self, parent, child):
        """Helper function for delete that moves a subtree of a deleted node
        into the correct position."""
        if parent.parent is None:
            self.root = child
        elif parent == parent.parent.left:
            parent.parent.left = child
        else:
            parent.parent.right = child
        if child is not None:
            child.parent = parent.parent

    def delete(self, data):
        """Find the node to delete. If the value specified by delete does NOT
        exist in the tree, then the function doesn't change the tree and
        instead raises a KeyError exception. If node found function utilizes
        transplant as needed to delete the node and adjust the tree."""
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and
        #  remove successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's
        # right subtree.
        # Note: Make sure to handle the case where the parent is None

        node = self.__find_node(data)
        try:
            if node is None:
                raise KeyError
        except KeyError:
            print("Given node does not exist in current Binary Search Tree")
            raise KeyError
        # The node is root
        if (node.left is None) and (node.right is None) and (node.parent is
        None):
            self.root = None
        # The node has no children and is not root
        elif (node.left is None) and (node.right is None):
            parent = node.parent
            if parent.right is node:
                parent.right = None
            else:
                parent.left = None
            return None
        # left node is only child
        elif node.left is None:
            # replace node with it's right child
            self.__transplant(node, node.right)
            return None
        # right node is only child
        elif node.right is None:
            # replace node with it's left child
            self.__transplant(node, node.left)
            return None
        else:
            succ = self.find_successor(node.data) # succ is node's successor
            if succ is not node.right:
                # replace succ with it's right child
                self.__transplant(succ, succ.right)
                # node's right child becomes succ right child
                succ.right = node.right
                succ.right.parent = succ
            # replace node with succ
            self.__transplant(node, succ)
            # node's left child given to succ which should have no left child
            # yet
            succ.left = node.left
            succ.left.parent = node
            return None



