def double_zero(array):
    arr = array
    for idx, i in enumerate(arr):
        if i == 0:
            arr.insert(idx + 1, 'flag')

    for idx, i in enumerate(arr):
        if i == 'flag':
            arr[idx] = 0

    print(arr)


double_zero([1, 0, 2, 3, 0, 4, 5, 0])
double_zero([1, 0, 2, 3, 0, 4, 5, 0])
double_zero([1, 2, 3])
