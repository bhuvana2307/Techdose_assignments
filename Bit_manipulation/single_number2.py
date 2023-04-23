class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        l=len(nums)
        nums.sort()
        c=0
        if l==1:
            return nums[0]
        if nums[0]!=nums[1]:
            c=1
            return nums[0]
        if nums[l-1]!=nums[l-2]:
            c=1
            return nums[l-1]
        if c==0:
            i=1
            while(1):
                if(nums[i]==nums[i-1]):
                    i+=3
                else:
                    return nums[i-1]
                if(i==l):
                    break