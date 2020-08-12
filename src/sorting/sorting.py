# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    i = 0
    j = 0

    len1 = len(arrA)
    len2 = len(arrB)

    arr = []

    while (i < len1) and (j < len2):
        
        if(arrA[i] < arrB[j]):
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1

    if i == len1:
        arr.extend(arrB[j:])
    else:
        arr.extend(arrA[i:])
    return arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Null case
    if len(arr) == 0:
        return None
    
    # Base case
    if len(arr) == 1:
        return arr

    # Recursive
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)   
        
        arr = merge(left, right)

        return arr

    # CONQUER
    # def merge_helper(a, b):
    #     sorted_arr = []
    #     ai = 0
    #     bi = 0
    #     while len(sorted_arr) < (len(a) + len(b)):
    #         if ai >= len(a):
    #             sorted_arr.append(b[bi])
    #             bi += 1
    #         elif bi >= len(b):
    #             sorted_arr.append(a[ai])
    #             ai += 1
    #         if a[ai] < b[bi]:
    #             sorted_arr.append(a[ai])
    #             ai += 1
    #         elif a[ai] >= b[bi]:
    #             sorted_arr.append(n[bi])
    #             bi += 1
        


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass