def selectionSort(arr):
    n = len(arr)
    for step in range(n):
        min_number = step

        for i in range(step + 1, n):
            if arr[i] < arr[min_number]:
                min_number = i
        arr[step], arr[min_number] = arr[min_number], arr[step]








if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    size = len(data)
    selectionSort(data)
    print('Sorted Array in Ascending Order:')
    print(data)