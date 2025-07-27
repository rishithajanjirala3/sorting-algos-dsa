#defination-->Quick Sort is a divide-and-conquer sorting algorithm that
#works by selecting a pivot element from the array and partitioning the other
#elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
#The sub-arrays are then recursively sorted.

def quicksort(arr):#T.C-O(nlogn) S.C-O(1)
    def qs(arr,low,high):
        if low<high:
            pIndex=partition(arr,low,high)
            qs(arr,low,pIndex-1)#recursively sort left part
            qs(arr,pIndex+1,high)#recursively sort right part
    def partition(arr,low,high):
        i=low
        j=high
        pivot=arr[low]#choosing first element and pivot

        # Rearrange elements around pivot
        while i<j:
            # Move i right until finding element > pivot
            while arr[i]<=pivot and i<high:
                i+=1
            # Move j left until finding element < pivot
            while arr[j]>=pivot and j>low:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]# # Swap out-of-place values
         # Place pivot in the correct position
        arr[low],arr[j]=arr[j],arr[low]
        return j # Return the pivot index
   
    #initial call to quicksort
    n=len(arr)
    low=0
    high=n-1
    qs(arr,low,high)
    return arr
arr=list(map(int,input().split()))
print("sorted array:",quicksort(arr))

