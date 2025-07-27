# Bubble Sort Function: Pushes the maximum element to the end in each pass using adjacent swaps
def bubblesort(arr,n):
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(bubblesort(arr,n))

#optimal bubble sort
def bubblesort(arr, n):
    # Outer loop: run from last index to the first index
    for i in range(n - 1, -1, -1):
        swapped = False  # To track if any swap happened in this pass

        # Inner loop: compare adjacent elements up to index i
        for j in range(i):
            # If current element is greater than the next one, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set flag to True as swap occurred

        # If no swaps happened in the current pass, array is already sorted
        if not swapped:
            break  # Exit early for efficiency

    return arr  # Return the sorted array
arr=list(map(int,input().split()))
n=len(arr)
print(bubblesort(arr,n))



