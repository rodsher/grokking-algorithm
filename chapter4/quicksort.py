def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [ i for i in arr[1:] if i < pivot ]
        greater = [ i for i in arr[1:] if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


l = [5, 10, 0, 15, 25, 40, 20]

print(quicksort(l))
