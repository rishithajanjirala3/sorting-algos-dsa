#selection sort
#defination-we need to select an min ele swap it with initail position

def selection(arr,n):#T.C-O(n^2) ,S.C-O(1)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(selection(arr,n))                                                                    