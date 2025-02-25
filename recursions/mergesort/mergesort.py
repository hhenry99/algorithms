def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a single element is already sorted

    mid = len(arr) // 2  # Find the middle index
    left = merge_sort(arr[:mid])  # Recursively sort left half
    right = merge_sort(arr[mid:])  # Recursively sort right half

    return merge(left, right)

def merge(left, right):
    merged_arr = []  # Initialize an empty array to store merged result
    l, r = 0, 0  # Pointers for left and right arrays

    # Merge elements from left and right into merged_arr in sorted order
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1

    # Append any remaining elements from left or right
    merged_arr.extend(left[l:])
    merged_arr.extend(right[r:])

    return merged_arr

def main():
    arr = [38, 27, 43, 3, 9, 82, 10]  # Sample array
    print("Original array:", arr)
    
    sorted_arr = merge_sort(arr)  # Perform Merge Sort
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
