def countingSort(arr, place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = arr[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10 - 1] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = output[i]


def radixSort(arr):
    max_number = max(arr)
    place = 1
    while max_number // place > 0:
        countingSort(arr, place)
        place *= 10


if __name__ == "__main__":
    data = [121, 432, 564, 23, 1, 45, 788]
    radixSort(data)
    print(data)
