from unittest import TestCase, main
import SortingAlgorithms as sA


class TestSortingAlgorithms(TestCase):

    def setUp(self):
        print "Set up"
        self.lst = [(2, "a"), (1, "b"), (3, "c")]

    def tearDown(self):
        print "Tear down", "\n"

    def test_swap(self):
        print "Testing swap"
        x = int(self.lst[0][0])
        y = int(self.lst[1][0])
        sA.swap(self.lst, 0, 1)
        self.assertNotEqual(x, self.lst[0][0])
        self.assertNotEqual(y, self.lst[0][1])

    def test_bubble_sort(self):
        print "Bubble Sort"
        is_sorted = True
        self.lst = sA.bubble_sort(self.lst)
        for i in range(len(self.lst)-1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)

    def test_insertion_sort(self):
        print "Testing Insertion Sort"
        is_sorted = True
        self.lst = sA.insertion_sort(self.lst)
        for i in range(len(self.lst)-1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)

    def test_selection_sort(self):
        print "Testing Selection Sort"
        is_sorted = True
        self.lst = sA.selection_sort(self.lst)
        for i in range(len(self.lst)-1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)

    def test_merge_sort(self):
        print "Testing Merge Sort"
        is_sorted = True
        self.lst = sA.merge_sort(self.lst)
        for i in range(len(self.lst)-1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)

    def test_quick_sort(self):
        print "Testing Quick Sort"
        is_sorted = True
        self.lst = sA.quick_sort(self.lst, 0, len(self.lst) - 1)
        for i in range(len(self.lst) - 1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)

    def test_heap_sort(self):
        print "Testing Heap Sort"
        is_sorted = True
        self.lst = sA.heap_sort(self.lst)
        for i in range(len(self.lst)-1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)

    def test_comb_sort(self):
        print "Testing Comb Sort"
        is_sorted = True
        self.lst = sA.comb_sort(self.lst)
        for i in range(len(self.lst)-1):
            if not self.lst[i][0] <= self.lst[i + 1][0]:
                is_sorted = False
                break
        self.assertTrue(is_sorted)


if __name__ == '__main__':
    main()
