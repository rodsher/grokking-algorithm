import math

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)
        guess = arr[mid]

        print('low', low)
        print('high', high)
        print('mid', mid)
        print('guess', guess)

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

vector = []

for i in range(0, 100):
    vector.append(i)

print(binary_search(vector, 3))
            

