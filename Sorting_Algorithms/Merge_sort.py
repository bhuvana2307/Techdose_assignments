def merge(arr,leftarr,rightarr,left,right):
    i,j,k=0,0,0
    while(i<left and j<right):
        if(leftarr[i]<rightarr[j]):
            arr[k]=leftarr[i]
            k+=1
            i+=1
        else:
            arr[k]=rightarr[j]
            k+=1
            j+=1
#for remaining elements
    while i < left:
        arr[k] = leftarr[i]
        i += 1
        k += 1

    while j < right:
        arr[k] = rightarr[j]
        j += 1
        k += 1

    
def mergesort(arr,length):
    if(length==1):
        return
    l=0
    h=length-1
    mid=l+((h-l)//2)
    leftarr=[0]*(mid+1)
    rightarr=[0]*(length-mid-1)
    for i in range(0,mid+1):
        leftarr[i]=arr[i]
    for i in range(mid+1,length):
        rightarr[i-(mid+1)]=arr[i]
    mergesort(leftarr,mid+1)
    mergesort(rightarr,length-mid-1)
    merge(arr,leftarr,rightarr,mid+1,length-mid-1)

nums=[4,2,8,6,9,1,3,0]
length=len(nums)
mergesort(nums,length)
print(nums)
#Time complexity: O(nlogn)
#n for iteration of an elements in the array
#logn for In each iteration dividing the arr into partition