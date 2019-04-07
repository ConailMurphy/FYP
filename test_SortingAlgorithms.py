from unittest import TestCase, main
import SortingAlgorithms as sA


class TestSortingAlgorithms(TestCase):

    def setUp(self):
        print "Set up"
        self.list_1 = [(2, "a"), (1, "b"), (3, "c")]
        self.list_2 = [2, 1, 3]

    def tearDown(self):
        print "Tear down", "\n"

    def test_swap(self):
        print "Testing swap"
        x = int(self.list_1[0][0])
        y = int(self.list_1[1][0])
        sA.swap(self.list_1, 0, 1)
        self.assertNotEqual(x, self.list_1[0][0])
        self.assertNotEqual(y, self.list_1[0][1])
        self.assertRaises(IndexError, sA.swap, self.list_1, 0, 3)

    def test_bubble_sort(self):
        print "Bubble Sort"
        is_sorted = True
        self.list_1 = sA.bubble_sort(self.list_1)
        for i in range(len(self.list_1)-1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.bubble_sort, self.list_2)
        self.assertTrue(sA.decisions_made)

    def test_insertion_sort(self):
        print "Testing Insertion Sort"
        is_sorted = True
        self.list_1 = sA.insertion_sort(self.list_1)
        for i in range(len(self.list_1)-1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.insertion_sort, self.list_2)
        self.assertTrue(sA.decisions_made)

    def test_selection_sort(self):
        print "Testing Selection Sort"
        is_sorted = True
        self.list_1 = sA.selection_sort(self.list_1)
        for i in range(len(self.list_1)-1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.selection_sort, self.list_2)
        self.assertTrue(sA.decisions_made)

    def test_merge_sort(self):
        print "Testing Merge Sort"
        is_sorted = True
        self.list_1 = sA.merge_sort(self.list_1)
        for i in range(len(self.list_1)-1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.merge_sort, self.list_2)
        self.assertTrue(sA.decisions_made)

    def test_quick_sort(self):
        print "Testing Quick Sort"
        is_sorted = True
        self.list_1 = sA.quick_sort(self.list_1, 0, len(self.list_1) - 1)
        for i in range(len(self.list_1) - 1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.quick_sort, self.list_2, 0, len(self.list_2) - 1)
        self.assertTrue(sA.decisions_made)

    def test_heap_sort(self):
        print "Testing Heap Sort"
        is_sorted = True
        self.list_1 = sA.heap_sort(self.list_1)
        for i in range(len(self.list_1)-1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.heap_sort, self.list_2)
        self.assertTrue(sA.decisions_made)

    def test_comb_sort(self):
        print "Testing Comb Sort"
        is_sorted = True
        self.list_1 = sA.comb_sort(self.list_1)
        for i in range(len(self.list_1)-1):
            if not self.list_1[i][0] <= self.list_1[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)
        self.assertRaises(TypeError, sA.comb_sort, self.list_2)
        self.assertTrue(sA.decisions_made)


if __name__ == '__main__':
    main()
