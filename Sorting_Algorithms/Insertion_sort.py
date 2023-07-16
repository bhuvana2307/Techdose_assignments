def Insertion_sort(arr):
    length=len(arr)
    for i in range(1,length):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

nums=[4,1,6,8,0,3]
Insertion_sort(nums)
print(nums)
#Time Complexity: O(n2)