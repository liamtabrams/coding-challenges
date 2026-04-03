def quicksort(arr):
    """
    The following is a Python implementation of quick sort.
    The time complexity in the average case is O(nlogn) and O(n^2) in the worst case,
    which occurs when the pivot selection is poor, such as always choosing the smallest
    or largest element of the subarray. The space complexity of this version (which is
    the out-of-place version) is O(n) due to additional space needed for the extra list
    variables used.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)


def quicksort(arr, low, high):
    """
    The following is a Python implementation of quick sort.
    The time complexity in the average case is O(nlogn) and O(n^2) in the worst case,
    which occurs when the pivot selection is poor, such as always choosing the smallest
    or largest element of the subarray. The space complexity of this version (which is
    the in-place version) is O(logn). 
    """
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # Pivot (Element to be placed at the right position)
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i + 1
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print(f"Sorted array: {arr}")