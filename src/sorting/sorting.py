# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Break up the "divide" and "conquer"
    # Parts of this algorithm
    # DIVIDE - recursive
    # What is our base case?

    # What can we do to get closer to the base case? 

    return arr

    # CONQUER
    def merge_helper(a, b):
        # There are 4 cases we need to consider
        # When merging together our sorted
        # lists 'a' and 'b'

        # We return a single list htat contains elements of a, b merged in sorted order
        pass

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

