import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):

    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    def test_2_pq_full(self):
        print("Return IndexError if the queue is full.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        with self.assertRaises(Exception):
            pq.insert(6)
        print("\n")

    def test_3_pq_full_empty(self):
        # additional
        print("Return IndexError if the queue is full.")
        print("\n")
        pq = pqueue.pqueue(0)
        with self.assertRaises(Exception):
            pq.insert(1)
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max_empty(self):
        print("Raise KeyError if queue is empty")
        print("\n")
        pq = pqueue.pqueue(5)
        with self.assertRaises(Exception):
            pq.extract_max()
        print("\n")

    def test_3_pq_extract_max_unordered(self):
        # additional
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(2)
        pq.insert(1)
        pq.insert(3)
        l = []
        l.append(pq.extract_max())
        l.append(pq.extract_max())
        l.append(pq.extract_max())
        self.assertEqual(l, [3, 2, 1])
        print("\n")

class T3_build_heap(unittest.TestCase):

    def test_build_heap(self):
        print("\n")
        build_list = [10,20,5,40,4,65,28,77,7]
        heap = mheap.max_heap(len(build_list), build_list)
        heap.build_heap()

        self.assertEqual(heap.heap, [77, 40, 65, 20, 4, 5, 28, 10, 7])
        print("\n")

    def test_build_heap_multiple(self):
        # additional
        print("\n")
        build_list = [10, 20, 5, 40, 4, 65, 28, 77, 7]
        heap = mheap.max_heap(len(build_list), build_list)
        heap.build_heap()
        heap.build_heap()
        heap.build_heap()

        self.assertEqual(heap.heap, [77, 40, 65, 20, 4, 5, 28, 10, 7])
        print("\n")

class T4_pqueue_insert_extract_max(unittest.TestCase):

    def test_1_pq_insert_extract_max(self):
        # additional
        print("\n")
        pq = pqueue.pqueue(10)
        for i in range(0, 10):
            pq.insert(i)
        for i in range(0, 5):
            pq.extract_max()
        self.assertEqual(pq.peek(), 4)
        print("\n")


class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

    def test_heap_sort_empty(self):
        # additional
        print("\n")
        empty_list = []
        empty_list = mheap.heap_sort(empty_list)

        self.assertEqual(empty_list, [])
        print("\n")

    def test_heap_sort_duplicates(self):
        # additional
        print("\n")
        duplicate_list = [4, 4, 4, 3, 4, 3, 2, 1, 2, 3]
        duplicate_list = mheap.heap_sort(duplicate_list)

        self.assertEqual(duplicate_list, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        print("\n")

    
    
if __name__ == '__main__':
    unittest.main()