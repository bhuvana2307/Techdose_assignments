nums=[5,1,4,9,7,2]
n=len(nums)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(nums[j]>nums[j+1]):
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
#Time complexity:O(n2)