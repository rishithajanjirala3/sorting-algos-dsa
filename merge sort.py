#merging 2lists using 2 pointer tecnique
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
i=0
j=0
res=[]
while i<len(nums1) and j<len(nums2):
    if nums1[i]<=nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j+=1
while i<len(nums1):
    res.append(nums1[i])
    i+=1
while j<len(nums2):
    res.append(nums2[j])
    j+=1
print(res)

#MERGE SORT-T.C(O(nlogn))  S.C-O(n)
def mergeSort(arr,n):
    def mS(arr,low,high):
        if low==high:
            return
        mid=(low+high)//2
        mS(arr,low,mid)
        mS(arr,mid+1,high)
        sort(arr,low,mid,high)
    def sort(arr,low,mid,high):
        i=low
        j=mid+1
        k=[]
        while i<=mid and j<=high:
            if arr[i]<=arr[j]:
                k.append(arr[i])
                i+=1
            else:
                k.append(arr[j])
                j+=1
        while i<=mid:
            k.append(arr[i])
            i+=1
        while j<=high:
            k.append(arr[j])
            j+=1
        for ind,val in enumerate(k):
            arr[ind+low]=val
    low=0
    high=n-1
    mS(arr,low,high)
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(mergeSort(arr,n))
            
    