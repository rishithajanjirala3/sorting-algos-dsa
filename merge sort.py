#merging 2lists using 2 pointer tecnique
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
i=0#pointer 1
j=0#pointer 2
res=[]
# Compare elements from both lists and merge
while i<len(nums1) and j<len(nums2):
    if nums1[i]<=nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j+=1
# If any elements remain in nums1
while i<len(nums1):
    res.append(nums1[i])
    i+=1
# If any elements remain in nums2
while j<len(nums2):
    res.append(nums2[j])
    j+=1
print('Merge list:'res)

#MERGE SORT-T.C(O(nlogn))  S.C-O(n)
def mergeSort(arr,n):
    def mS(arr,low,high):
        if low==high:
            return
        mid=(low+high)//2
        mS(arr,low,mid)#sort left half
        mS(arr,mid+1,high)#sort right half
        sort(arr,low,mid,high)#merge both halves
    def sort(arr,low,mid,high):
        i=low
        j=mid+1
        temp=[]
         # Merge the two sorted halves into temp[]
        while i<=mid and j<=high:
            if arr[i]<=arr[j]:
                k.append(arr[i])
                i+=1
            else:
                k.append(arr[j])
                j+=1
        # Copy remaining elements from left half
        while i<=mid:
            k.append(arr[i])
            i+=1
        # Copy remaining elements from right half
        while j<=high:
            k.append(arr[j])
            j+=1
         # Copy sorted temp[] back into arr
        for ind,val in enumerate(k):
            arr[ind+low]=val
    low=0
    high=n-1
    mS(arr,low,high)
    return arr

#example usage
arr=list(map(int,input().split()))
n=len(arr)
print('sorted list:',mergeSort(arr,n))
            
    
