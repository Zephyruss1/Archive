def shellSort(arr, n):
    interval = int(n / 2)   # 1. Initialize interval as size / 2
    while interval > 0:
        for i in range(0, n):
            temp = arr[i]   # 2. Pick elements from interval to the end
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2


if __name__ == '__main__':
    data = [9, 8, 3, 7, 5, 6, 4, 1]
    size = len(data)
    shellSort(data, size)
    print('Sorted Array in Ascending Order:')
    print(data)
