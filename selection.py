# Definition: In Selection Sort, we repeatedly find the minimum element 
# from the unsorted part and put it at the beginning.

# Time Complexity: O(n^2)
# Space Complexity: O(1) - in-place sorting

def selection(arr,n):
    for i in range(0,n):
        min=i # Assume current index has the minimum

        # Find index of the smallest element in remaining array
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        # Swap the found minimum with the first element of unsorted part
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(selection(arr,n))                                                                    
