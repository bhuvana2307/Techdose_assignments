nums=[0,8,3,1,6,3,2,8]
length=len(nums)
for i in range(0,length):
    midindx=i 
    for j in range(i+1,length):
        if(nums[midindx]>nums[j]):
            midindx=j 
    #swapping
    nums[i],nums[midindx]=nums[midindx],nums[i]
print(nums)
#Time complexity: O(n2)