#defination-push the max element to the last by adj swap
def bubblesort(arr,n):
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(bubblesort(arr,n))