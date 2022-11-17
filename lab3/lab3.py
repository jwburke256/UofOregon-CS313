class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
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
        # returns the node with that particular data value else returns None
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
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        found = self.__find_node(data)
        if found is None:
            return False
        else:
            return True

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, 1)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, 2)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, 3)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        
        #Yield data of the correct node/s
        if curr_node is not None:
            if traversal_type is 1:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type is 2:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type is 3:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data
        else:
            return None

    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        node = self.__find_node(data)
        try:
            if node is None:
                raise KeyError
        except KeyError:
            print("Given node does not exist in current Binary Search Tree")
            raise KeyError
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
        if parent.parent is None:
            self.root = child
        elif parent == parent.parent.left:
            parent.parent.left = child
        else:
            parent.parent.right = child
        if child is None:
            child.parent = parent.parent

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None

        node = self.__find_node(data)
        try:
            if node is None:
                raise KeyError
        except KeyError:
            print("Given node does not exist in current Binary Search Tree")
            raise KeyError
        if node.left is None:
            self.__transplant(node, node.right)
        elif node.right is None:
            self.__transplant(node, node.left)
        else:
            y = self.min()
            if y is not node.right:
                self.__transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.__transplant(node, y)
            y.left = node.left
            y.left.parent = node
        return None



        # node = self.__find_node(data)
        # try:
        #     if node is None:
        #         raise KeyError
        # except KeyError:
        #     print("Given node does not exist in current Binary Search Tree")
        #     raise KeyError
        # # The node is root
        # if (node.left is None) and (node.right is None) and (node.parent is None):
        #     self.root = None
        # # The node has no children and is
        # elif (node.left is None) and (node.right is None):
        #     node.parent = None
        # # The node has one child
        # elif ((node.left is not None) and (node.right is None)) or ((node.left is None) and (node.right is not None)):
        #     if node.left is not None:
        #         child = node.left
        #         parent = node.parent
        #         parent.


