import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

    def test_unbalanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(1)
        t.insert(2)
        t.insert(3)
        t.insert(4)
        t.insert(5)
        t.insert(6)
        t.insert(7)
        maximum = t.max()

        self.assertEqual(t.root.data, 1)
        self.assertEqual(t.root.left, None)
        self.assertEqual(t.root.right.data, 2)
        self.assertEqual(t.root.right.right.data, 3)
        self.assertEqual(t.root.right.right.right.right.data, 5)
        self.assertEqual(maximum, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checking the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

    def test_min_and_max_unbalanced_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(1)
        t.insert(2)
        t.insert(3)
        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 3)


class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")

    def test__traverse(self):
        print("\n")
        print("Checking all the three traverses")
        t = lab3.Tree()
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        tree_inorder = [node for node in t._Tree__traverse(t.root, 1)]
        tree_preorder = [node for node in t._Tree__traverse(t.root, 2)]
        tree_postorder = [node for node in t._Tree__traverse(t.root, 3)]

        print("inorder traversal")
        self.assertEqual(tree_inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(tree_preorder, [4, 2, 1, 3, 6, 5, 7])
        print("postorder traversal")
        self.assertEqual(tree_postorder, [1, 3, 2, 5, 7, 6, 4])
        print("\n")


class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

    def test_successor_empty(self):
        print("\n")
        print("successor function on emptry tree")
        tree_success = lab3.Tree()
        with self.assertRaises(Exception):
            empty = tree_success.find_successor(8).data
        print("\n")

    def test_successor_single_node(self):
        print("\n")
        print("successor function with single node")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        none_success = tree_success.find_successor(8)

        self.assertEqual(none_success, None)


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete_empty(self):
        print("\n")
        print("delete function on empty tree")
        t = lab3.Tree()
        with self.assertRaises(Exception):
            deleted = t.delete(8)
        print("\n")

    def test_delete_node_not_in_tree(self):
        print("\n")
        print("delete function with a given node not in the tree")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)

        l1 = [node for node in t]
        self.assertEqual(l1, [1, 3, 4, 6, 8, 10])
        with self.assertRaises(Exception):
            deleted = t.delete(7)
        l2 = [node for node in t]
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10])


class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test_contains_empty_tree(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test__find_node(self):
        print("\n")
        print("find node private function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        node1 = t._Tree__find_node(1)
        node2 = t._Tree__find_node(6)
        node3 = t._Tree__find_node(5)

        self.assertEqual(node1.data, 1)
        self.assertEqual(node2.data, 6)
        self.assertEqual(node3, None)
        print("\n")



if __name__ == '__main__' :
    unittest.main()