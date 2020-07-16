def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        submax = max(arr[1:])
        return arr[0] if arr[0] > submax else submax

print(max([5, 10, 15, 20, 25, 30, 35, 700,  40]))
