def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if (array[i] < array[j]):
                array[j], array[i] = array[i], array[j]
                i = i - 1
                continue
            break

    return array
