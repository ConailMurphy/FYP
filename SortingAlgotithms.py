import itertools
to_sort = [1, 8, 3, 9, 4, 5, 7]
comparisons = []
array_history = []

def swap(array, x, y):
    array[x], array[y] = array[y], array[x]


def bubble_sort(array):
    for i in range(len(array)):

        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                comparisons.append((array[j], ">", array[j+1]))
                swap(array, i, j)
                array_history.append(list(array))
            else:
                comparisons.append((array[j], "<", array[j+1]))
                array_history.append(list(array))
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            comparisons.append((key, "<", array[j]))
            array[j+1] = array[j]
            j -= 1
            array_history.append(list(array))
        comparisons.append((key, ">", array[j]))
        array[j+1] = key
        array_history.append(list(array))
    return array


def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[minimum] > array[j]:
                comparisons.append((array[minimum], ">", array[j]))
                array_history.append(list(array))
                minimum = j
            else:
                comparisons.append((array[minimum], "<", array[j]))
                array_history.append(list(array))
        swap(array, i, minimum)
    return array


def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        left_array = merge_sort(array[:midpoint])
        right_array = merge_sort(array[midpoint:])

        merged_array = merge(left_array, right_array)
        array_history.append(list(merged_array))
        return merged_array
    array_history.append(list(array))
    return array


def merge(left_array, right_array):
    merged_array = []
    while len(left_array) != 0 and len(right_array) != 0:

        if left_array[0] < right_array[0]:
            comparisons.append((left_array[0], "<", right_array[0]))
            merged_array.append(left_array[0])
            left_array.remove(left_array[0])
        else:
            merged_array.append(right_array[0])
            comparisons.append((left_array[0], ">", right_array[0]))
            right_array.remove(right_array[0])

    if len(left_array) > 0:
        merged_array += left_array

    elif len(right_array) > 0:
        merged_array += right_array
    return merged_array


def quick_sort_start(array):
    array = quick_sort(array, 0, len(array) - 1)
    return array


def quick_sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)

        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)
    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            comparisons.append((array[j], "<", pivot))
            i += 1
            swap(array, i, j)
            array_history.append(list(array))

        else:
            comparisons.append((array[j], ">", pivot))
            array_history.append(list(array))
    swap(array, i+1, high)
    # array_history.append(list(array))
    return i+1


def heap_sort(array):

    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array_history.append(list(array))
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    array_history.append(list(array))
    return array


def heapify(array, n, i):
    maximum = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and array[i] < array[left_child]:
        comparisons.append((array[left_child], ">", array[i]))
        maximum = left_child
    elif left_child < n and array[i] > array[left_child]:
        comparisons.append((array[left_child], "<", array[i]))

    if right_child < n and array[maximum] < array[right_child]:
        comparisons.append((array[right_child], ">", array[maximum]))
        maximum = right_child
    elif right_child < n and array[maximum] > array[right_child]:
        comparisons.append((array[right_child], "<", array[maximum]))

    if maximum != i:
        array_history.append(list(array))
        array[i], array[maximum] = array[maximum], array[i]
        heapify(array, n, maximum)


def sort(sorting_algorithm, a_list):
    results = []
    # list_permutations = []
    #
    # for k in itertools.permutations(a_list, r=len(a_list)):
    #     list_permutations.append(k)
    #
    # for l in list_permutations:
    #     initial_array = list(l)
    #     sorted_array = sorting_algorithm(list(initial_array))
    #     results.append((initial_array, sorted_array, list(comparisons), list(array_history)))
    #     del comparisons[:]
    #     del array_history[:]

    initial_array = list(a_list)
    sorted_array = sorting_algorithm(list(a_list))
    results.append((initial_array, sorted_array, comparisons, list(array_history)))

    for r in results:
        print(len(r[2]), len(r[3]))
    #     print("\n")




sort(heap_sort, to_sort)