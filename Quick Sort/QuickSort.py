def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            # if element smaller than the pivot is found, 
            # swap it with greater element at ith index
            i += 1
            array[i], array[j] = array[j], array[i]

    # swap pivot with element e greater than specified i
    array[i+1], array[high] = array[high], array[i+1]

    return i + 1


def quicksort(array, low, high):

    if low < high:
        pi = partition(array, low, high)

        quicksort(array, low, pi - 1)
        quicksort(array, pi+1, high)