class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=0
        c=0
        res=x^y
        b=bin(res)
        c=b.count('1')
        return c