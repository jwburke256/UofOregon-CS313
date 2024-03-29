# only need to write docstrings for left_rotate, right_rotate, insert_fixup, delete_fixup

class Node(object):
    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """Red Black Tree

            Supports most standard Red Black Tree operations (print_tree, find_node, find_successor,
            insert, delete). Can be used for storing integer data in a sorted order, and then able to
            be printed out in a specified manner with calling the desired traversal
            method (inorder, preorder, postorder). Tree has a maximum height of
            log n, as well as the ability to self balance when needed.
            ...


            Attributes
            ----------
            root: int
                first node in the Binary Search Tree
            sentinel : Node
                sentinel node that contains node data, with the only characterstic being black color
            sentinel.parent: Node
                further set up sentinel node
            sentinel.left: Node
                further set up sentinel node
            sentinel.right: Node
                further set up sentinel node

            Methods
            -------
            left_rotate(node):
                Function used in conjunction with insert and delete in order to balance the
                tree nodes by performing a left rotate operation with a given node. The function
                raises an exception if the root is empty.
            right_rotate(node):
                Function used in conjunction with insert and delete in order to balance the
                tree nodes by performing a right rotate operation with a given node. The function
                raises an exception if the root is empty.
            __rb_insert_fixup(node):
                after inserting a new node to a tree, the __rb_insert_fixup function is called in
                order to rebalance/recolor the nodes as needed in order to maintain the
                Red/Black tree properties. The function goes through 4 different possible test cases
                and will progress through the tree until balance is achieved.
            __rb_delete_fixup(self, x):
                after deleting a node from the tree, the  __rb_delete_fixup function is called in
                order to rebalance/recolor the remaining nodes as needed in order to maintain the
                Red/Black tree properties. The function goes through 4 different possible test cases
                and will progress through the tree until balance is achieved once again.
            """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color is "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        return self.inorder()

    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    # put adds a node to the tree
    def insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    
    def delete(self, data):
        # Same as binary tree delete, except we call rb_delete fixup at the end.

        z = self.find_node(data)
        if z.left is self.sentinel or z.right is self.sentinel:
            y = z
        else:
            y = self.find_successor(z.data)
        
        if y.left is not self.sentinel:
            x = y.left
        else:
            x = y.right
        
        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        
        if y is not z:
            z.data = y.data
    
        if y.color == 'black':
            if x is self.sentinel:
                self.__rb_delete_fixup(y)
            else:
                self.__rb_delete_fixup(x)

    def left_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # if x is the root of the tree to rotate with left child subtree T1 and right child y, 
        # where T2 and T3 are the left and right children of y then:
        # x becomes left child of y and T3 as its right child of y
        # T1 becomes left child of x and T2 becomes right child of x

        # refer page 328 of CLRS book for rotations

        try:
            if self.root is None:
                raise KeyError
        except KeyError:
            print("Given node does not have required node to perform rotation")
            raise KeyError
        y = current_node.right
        current_node.right = y.left
        if y.left != self.sentinel:
            y.left.parent = current_node
        y.parent = current_node.parent
        if current_node.parent == self.sentinel:
            self.root = y
        elif current_node == current_node.parent.left:
            current_node.parent.left = y
        else:
            current_node.parent.right = y
        y.left = current_node
        current_node.parent = y
    
    def right_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # If y is the root of the tree to rotate with right child subtree T3 and left child x, 
        # where T1 and T2 are the left and right children of x then:
        # y becomes right child of x and T1 as its left child of x
        # T2 becomes left child of y and T3 becomes right child of y

        # refer page 328 of CLRS book for rotations

        try:
            if self.root is None:
                raise KeyError
        except KeyError:
            print("Given node does not have required node to perform rotation")
            raise KeyError
        y = current_node.left
        current_node.left = y.right
        if y.right != self.sentinel:
            y.right.parent = current_node
        y.parent = current_node.parent
        if current_node.parent == self.sentinel:
            self.root = y
        elif current_node == current_node.parent.right:
            current_node.parent.right = y
        else:
            current_node.parent.left = y
        y.right = current_node
        current_node.parent = y

    
    def __rb_insert_fixup(self, z):
        # This function maintains the balancing and coloring property after bst insertion into
        # the tree. Please red the code for insert() method to get a better understanding
        # refer page 330 of CLRS book and lecture slides for rb_insert_fixup

        while z.parent.color is "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color is "red": # Case 1
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right: # Case 2
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            # Case 4
            else:
                y = z.parent.parent.left
                if y.color is "red":  # Case 1
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:  # Case 2
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"


    def __rb_delete_fixup(self, x):
        # This function maintains the balancing and coloring property after bst deletion 
        # from the tree. Please read the code for delete() method to get a better understanding.
        # refer page 338 of CLRS book and lecture slides for rb_delete_fixup
        
        while (x is not self.root) and (x.color is "black"):
            if x is x.parent.left:
                w = x.parent.right
                if w.color is "red": # Case 1
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if (w.left.color is "black") and (w.right.color is "black"): # Case 2
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color is "black": # Case 3
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    # Case 4 (always follows Case 3)
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if (w.right.color is "black") and (w.left.color is "black"):
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color is "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"



    


    
    