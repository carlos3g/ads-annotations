def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while (low <= high):
        mid = (low + high) // 2

        if (target == array[mid]):
            return mid

        if (target < array[mid]):
            high = mid - 1

        if (array[mid] < target):
            low = mid + 1

    return -1
