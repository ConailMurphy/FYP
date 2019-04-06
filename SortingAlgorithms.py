# sorting algorithms take an array of tuples as input
# the tuples must be in the format (n, l), such that n is a number
# and l is a letter where the first tuple in the list would have l = "a"
# the second would have l = "b" and so on
# this is for bookkeeping purposes so the results can be used to build the decision tree

# whenever a sorting algorithm makes a comparison, it will be appended to this list
decisions_made = []


# function for swapping two given indexes in a list
def swap(array, x, y):
    array[x], array[y] = array[y], array[x]


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j][0] > array[j+1][0]:
                decisions_made.append((str(array[j][1]), ">", str(array[j+1][1])))
                swap(array, j, j+1)
            else:
                decisions_made.append((str(array[j][1]), "<", str(array[j+1][1])))
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key[0] < array[j][0]:
            decisions_made.append((str(key[1]), "<", str(array[j][1])))
            swap(array, j+1, j)
            j -= 1
        decisions_made.append((str(key[1]), ">", str(array[j][1])))
        array[j+1] = key
    return array


def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[minimum][0] > array[j][0]:
                decisions_made.append((str(array[minimum][1]), ">", str(array[j][1])))
                minimum = j
            else:
                decisions_made.append((str(array[minimum][1]), "<", str(array[j][1])))
        swap(array, i, minimum)
    return array


def merge_sort(array):
    if len(array) > 1:
        if len(array) > 1:
            midpoint = len(array) // 2
            left_array = merge_sort(array[:midpoint])
            right_array = merge_sort(array[midpoint:])
            merged_array = merge(left_array, right_array)
            return merged_array
    return array


def merge(left_array, right_array):
    merged_array = []
    while len(left_array) != 0 and len(right_array) != 0:
        if left_array[0][0] < right_array[0][0]:
            decisions_made.append((str(left_array[0][1]), "<", str(right_array[0][1])))
            merged_array.append(left_array[0])
            left_array.remove(left_array[0])
        else:
            merged_array.append(right_array[0])
            decisions_made.append((str(left_array[0][1]), ">", str(right_array[0][1])))
            right_array.remove(right_array[0])

    if len(left_array) > 0:
            merged_array += left_array
    elif len(right_array) > 0:
        merged_array += right_array

    return merged_array


def quick_sort(array, low, high):
    if low < high:
            partition_index = partition(array, low, high)
            quick_sort(array, low, partition_index - 1)
            quick_sort(array, partition_index + 1, high)
    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j][0] <= pivot[0]:
            decisions_made.append((array[j][1], "<", pivot[1]))
            i += 1
            swap(array, i, j)
        else:
            decisions_made.append((array[j][1], ">", pivot[1]))
    swap(array, i+1, high)
    return i + 1


def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        swap(array, i, 0)
        heapify(array, i, 0)
    return array


def heapify(array, n, i):
    maximum = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and array[i][0] < array[left_child][0]:
        decisions_made.append((array[left_child][1], ">", array[i][1]))
        maximum = left_child
    elif left_child < n and array[i][0] > array[left_child][0]:
        decisions_made.append((array[left_child][1], "<", array[i][1]))

    if right_child < n and array[maximum][0] < array[right_child][0]:
        decisions_made.append((array[right_child][1], ">", array[maximum][1]))
        maximum = right_child
    elif right_child < n and array[maximum][0] > array[right_child][0]:
        decisions_made.append((array[right_child][1], "<", array[maximum][1]))

    if maximum != i:
        array[i], array[maximum] = array[maximum], array[i]
        heapify(array, n, maximum)
