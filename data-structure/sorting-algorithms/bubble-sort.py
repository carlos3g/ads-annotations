def bubble_sort(array):
    while (True):
        is_sorted = True

        for i in range(len(array) - 1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if (is_sorted):
            break

    return array
