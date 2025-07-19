#defination-takes an element and place at correct position
def insertion(arr,n):
    for i in range(0,n):
        while i>0 and arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(insertion(arr,n))