def countingSort(arr):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = output[i]


if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    countingSort(data)
    print("Sorted Array in Ascending Order: ")
    print(data)
