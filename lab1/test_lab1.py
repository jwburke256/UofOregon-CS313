import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):
    def test_basic_enqueue_str(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

class T1_TestingQueue(unittest.TestCase):
    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        q = lab1.Queue()
        q.enqueue("4")
        print("return false if the Queue is not empty")
        self.assertEqual(q.isEmpty(), False)
        print("\n")

class T2_TestingQueue(unittest.TestCase):
    def test_is_empty_true(self):
        # testing if queue is empty
        print("\n")
        q = lab1.Queue()
        print("return true if the Queue is empty")
        self.assertEqual(q.isEmpty(), True)
        print("\n")

class T3_TestingQueue(unittest.TestCase):
    def test_basic_dequeue(self):
        # testing the basic push operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.__str__(), '[2, 3]')
        print("\n")

class T4_TestingStack(unittest.TestCase):
    def test_basic_stack_str(self):
        # testing the basic push operation
        print("\n")
        s = lab1.Stack()
        s.push(4)
        s.push(3)
        s.push(2)
        s.push(1)

        self.assertEqual(s.__str__(), '[1, 2, 3, 4]')
        print("\n")

class T5_TestingStack(unittest.TestCase):
    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

class T6_TestingStack(unittest.TestCase):
    def test_is_empty_true(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        print("return true if the stack is empty")
        self.assertEqual(s.isEmpty(), True)
        print("\n")

class T7_TestingStack(unittest.TestCase):
    def test_basic_stack_pop(self):
        # testing the basic push operation
        print("\n")
        s = lab1.Stack()
        s.push(1)
        s.push(2)

        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.__str__(), '[1]')
        print("\n")

class T8_TestingStack(unittest.TestCase):
    def test_stack_empty_pop(self):
        # testing the basic push operation
        print("\n")
        s = lab1.Stack()

        self.assertEqual(s.pop(), None)
        print("\n")


class T9_TestingPalindrome(unittest.TestCase):
    def test_basic_string_nonpal(self):
        # testing with basic non-palindrome string
        print("\n")
        string = "Hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

class T10_TestingPalindrome(unittest.TestCase):
    def test_basic_string_pal(self):
        # testing with basic palindrome string
        print("\n")
        string = "mygym"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

class T11_TestingPalindrome(unittest.TestCase):
    def test_string_with_spaces(self):
        # testing with basic palindrome string
        print("\n")
        string = "ni t I n"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

class T12_TestingPalindrome(unittest.TestCase):
    def test_string_final_case(self):
        # testing with basic palindrome string
        print("\n")
        string = "TaCo CaT"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

if __name__ == '__main__':
    unittest.main()
