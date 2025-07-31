import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot] 
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 

    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(equal))
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(quick_select(arr, k))