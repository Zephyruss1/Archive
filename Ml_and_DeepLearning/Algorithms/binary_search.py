def binarySearch(arr, l, h, x):
    while l <= h:
        mid = l + (h - l) // 2  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            h = mid - 1

    return -1


# Driver Code
if __name__ == '__main__':
    arr = [3, 4, 5, 6, 7, 8, 9]
    x = 4

    # Function call
    result = binarySearch(arr, x, 0, len(arr) - 1)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
