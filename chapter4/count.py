def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])

print(count([5, 10, 15, 20]))
