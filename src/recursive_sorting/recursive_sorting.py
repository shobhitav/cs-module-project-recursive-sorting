# TO-DO: complete the helper function below to merge 2 sorted arrays
'''  DESCRIPTION OF MERGE -SORT ALGORITHM
(time complexity :O(n logn) , space complexity : O(n))

DIVIDE AND CONQUER  
1. 'divide array in half until you have n subarrays of length 1'
	all these subarrays are already sorted

2. 'take 2 sequential subarrays and sort them'
	look at the front of each array
	remove the lowest number, add it to a marged subarray
	repeat until both arrays are empty

3. 'move on to the next two subarrays and repeat the previous step'

4. 'move back to the beginning of the array and repeat steps 2 and 3'

5. 'return sorted array'  
'''

'''CONQUER: Keep checking first elements of left and right arrays and keep appending the sorted array .
'''
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    for i in range(len(merged_arr)):
    
        # LHS is empty( so copy the RHS  to merged_arr)
        if len(arrA) == 0:
            merged_arr[i]=arrB[0]
            # remove the first element of right array.
            arrB.pop(0)  
        # RHS is empty ( so copy the LHS  to merged_arr)
        elif len(arrB) == 0:
            merged_arr[i]= arrA[0]
            arrA.pop(0)
        #1. front of lhs < front of rhs , then add the front of lhs to merged_arr. 
        # and to keep track of front of elements , remove the added element from lhs array(arrA here)
        elif arrA[0] < arrB[0]:
            merged_arr[i]=arrA[0]
            arrA.pop(0)
        #1. front of rhs < front of lhs , then add the front of rhs to merged_arr. 
        # and to keep track of front of elements , remove the added element from rhs array(arrB here)
        elif arrB[0] < arrA[0]:
            merged_arr[i]=arrB[0]
            arrB.pop(0)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

'''
# 1.DIVIDE ---- Break the list into half until length of list is 1 (single element is always sorted)
	# all these subarrays are already sorted. For an array of N elements , it takes log N steps 
    # to divide it into single element array. 
# function merge_sort does that .
'''
def merge_sort(arr):
    # base case(sorted list)
    if len(arr)<=1:
        return arr
    
    # recursive case(Keep dividing till base case is reached) 
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)




# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
