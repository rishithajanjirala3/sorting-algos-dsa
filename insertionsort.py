#defination-takes an element and place at correct position
def insertion(arr,n):#T.C-	O(n²),S.C-O(1)
    for i in range(0, n):
        # Move the current element to its correct position by swapping with previous larger elements
        while i > 0 and arr[i - 1] > arr[i]:
            # Swap if the previous element is greater than current
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr
       
arr=list(map(int,input().split()))
n=len(arr)
print('sorted array:',insertion(arr,n))
