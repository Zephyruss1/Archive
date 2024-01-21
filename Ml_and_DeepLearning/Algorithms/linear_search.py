def linearSearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    array = [2, 4, 0, 1, 9]
    x = 1
    n = len(array)
    result = linearSearch(array, n, x)
    if (result == -1):
        print("Element not found")
    else:
        print("Element found at index: ", result)
