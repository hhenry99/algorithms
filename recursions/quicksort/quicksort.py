def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as the pivot
    i = low
    j = high

    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[low], arr[j] = arr[j], arr[low]  # Place pivot in the correct position
    return j  # Return the pivot index

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array:", arr)