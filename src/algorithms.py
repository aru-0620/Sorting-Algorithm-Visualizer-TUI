import random

# Bubble Sort


def Bubble_Sort(array):
    n = len(array)
    Swap = True

    while Swap:
        Swap = False

        for i in range(n - 1):
            yield {"comparing": [i, i + 1], "swaping": [], "array": array.copy()}

            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                Swap = True

                yield {"comparing": [], "swaping": [i, i + 1], "array": array.copy()}
    yield {"comparing": [], "swaping": [], "array": array.copy()}


# Quick_Sort


def Quick_Sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low >= high:
        yield {"array": array.copy(), "comparing": [], "swaping": []}
        return

    pivot = array[(low + high) // 2]
    i, j = low, high

    while i <= j:
        while i <= high and array[i] < pivot:
            yield {"array": array.copy(), "comparing": [i], "swaping": []}
            i += 1

        while j >= low and array[j] > pivot:
            yield {"array": array.copy(), "comparing": [j], "swaping": []}
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            yield {"array": array.copy(), "comparing": [], "swaping": [i, j]}
            i += 1
            j -= 1
    if low < j:
        yield from Quick_Sort(array, low, j)

    if i < high:
        yield from Quick_Sort(array, i, high)


# Merge Sort


def Merge_Sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left >= right:
        return

    mid = (left + right) // 2

    yield from Merge_Sort(array, left, mid)
    yield from Merge_Sort(array, mid + 1, right)
    yield from Merge(array, left, mid, right)


def Merge(array, left, mid, right):
    left_part = array[left : mid + 1]
    right_part = array[mid + 1 : right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        yield {"array": array.copy(), "comparing": [k], "swaping": []}

        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1

        yield {"array": array.copy(), "comparing": [], "swaping": [k]}

        k += 1

    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1
        yield {"array": array.copy(), "comparing": [], "swaping": [k - 1]}

    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1
        yield {"array": array.copy(), "comparing": [], "swaping": [k - 1]}


# Heap Sort


def Heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        yield {"array": array.copy(), "comparing": [i, left], "swaping": []}
        if array[left] > array[largest]:
            largest = left

    if right < n:
        yield {"array": array.copy(), "comparing": [largest, right], "swaping": []}
        if array[right] > array[largest]:
            largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        yield {"array": array.copy(), "comparing": [], "swaping": [i, largest]}
        yield from Heapify(array, n, largest)


def Heap_Sort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        yield from Heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        yield {"array": array.copy(), "comparing": [], "swaping": [0, i]}
        yield from Heapify(array, i, 0)


# Bogo_Sort


def Bogo_Sort(array, max_shuffles=500):
    n = len(array)

    for _ in range(max_shuffles):
        # check if sorted
        sorted_flag = True
        for i in range(n - 1):
            yield {"comparing": [i, i + 1], "swaping": []}
            if array[i] > array[i + 1]:
                sorted_flag = False
                break

        if sorted_flag:
            return

        for i in range(n):
            j = random.randrange(n)
            array[i], array[j] = array[j], array[i]
            yield {"comparing": [], "swaping": [i, j]}
