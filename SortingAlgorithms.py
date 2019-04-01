# swap two given indexes in an array
def swap(array, x, y):
    array[x], array[y] = array[y], array[x]


def bubble_sort(array):
    array_to_sort = [(array[0], "a"), (array[1], "b"), (array[2], "c")]

    for i in range(len(array_to_sort)):
        for j in range(0, len(array_to_sort)-i-1):
            if array_to_sort[j][0] > array_to_sort[j+1][0]:
                swap(array_to_sort, j, j+1)

    return [(array[0], array_to_sort[0][1]), (array[1], array_to_sort[1][1]), (array[2], array_to_sort[2][1])]


def insertion_sort(array):
    array_to_sort = [(array[0], "a"), (array[1], "b"), (array[2], "c")]

    for i in range(1, len(array)):
        key = array_to_sort[i]
        j = i - 1
        while j >= 0 and key[0] < array_to_sort[j][0]:
            swap(array_to_sort, j+1, j)
            j -= 1
        array_to_sort[j+1] = key

    return [(array[0], array_to_sort[0][1]), (array[1], array_to_sort[1][1]), (array[2], array_to_sort[2][1])]


def selection_sort(array):
    array_to_sort = [(array[0], "a"), (array[1], "b"), (array[2], "c")]

    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array_to_sort[minimum][0] > array_to_sort[j][0]:
                minimum = j

        swap(array_to_sort, i, minimum)

    return [(array[0], array_to_sort[0][1]), (array[1], array_to_sort[1][1]), (array[2], array_to_sort[2][1])]


def merge_sort(array):
    if len(array) == 3:
        array_to_sort = [(array[0], "a"), (array[1], "b"), (array[2], "c")]

    if len(array) > 1:
        midpoint = len(array) // 2
        left_array = merge_sort(array[:midpoint])
        right_array = merge_sort(array[midpoint:])

        merged_array = merge(left_array, right_array)

        if len(array) == 3:
            sort_results = []

            for i in range(len(merged_array)):
                for j in range(len(array_to_sort)):
                    if merged_array[i] == array_to_sort[j][0]:
                        sort_results.append((merged_array[i], array_to_sort[j][1]))
                        array_to_sort.pop(j)
                        break

            return [(array[0], sort_results[0][1]), (array[1], sort_results[1][1]), (array[2], sort_results[2][1])]
        return merged_array
    return array


def merge(left_array, right_array):
    merged_array = []
    while len(left_array) != 0 and len(right_array) != 0:

        if left_array[0] <= right_array[0]:
            merged_array.append(left_array[0])
            left_array.remove(left_array[0])
        else:
            merged_array.append(right_array[0])
            right_array.remove(right_array[0])

    if len(left_array) > 0:
        merged_array += left_array

    elif len(right_array) > 0:
        merged_array += right_array
    return merged_array


def quick_sort(array, low, high, depth):
    initial_array = list(array)
    array_to_sort = [(array[0], "a"), (array[1], "b"), (array[2], "c")]

    if low < high:
        partition_index = partition(array, low, high)

        quick_sort(array, low, partition_index-1, depth+1)
        quick_sort(array, partition_index+1, high, depth+1)

    if depth == 0:
        sort_results = []

        for i in range(len(array)):
            for j in range(len(array_to_sort)):
                if array[i] == array_to_sort[j][0]:
                    sort_results.append((array[i], array_to_sort[j][1]))
                    array_to_sort.pop(j)
                    break

        return [(initial_array[0], sort_results[0][1]), (initial_array[1], sort_results[1][1]),
                (initial_array[2], sort_results[2][1])]
    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if pivot > array[j]:
            i += 1
            swap(array, i, j)
    swap(array, i+1, high)
    return i+1


def heap_sort(array):
    sort_results = []
    initial_array = list(array)
    array_to_sort = [(array[0], "a"), (array[1], "b"), (array[2], "c")]
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    for i in range(len(array)):
        for j in range(len(array_to_sort)):
            if array[i] == array_to_sort[j][0]:
                sort_results.append((array[i], array_to_sort[j][1]))
                array_to_sort.pop(j)
                break
    return [(initial_array[0], sort_results[0][1]), (initial_array[1], sort_results[1][1]),
            (initial_array[2], sort_results[2][1])]


def heapify(array, n, i):
    maximum = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and array[i] < array[left_child]:
        maximum = left_child

    if right_child < n and array[maximum] < array[right_child]:
        maximum = right_child

    if maximum != i:
        array[i], array[maximum] = array[maximum], array[i]
        heapify(array, n, maximum)