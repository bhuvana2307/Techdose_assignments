class Solution:
    def decode(self, enc: list[int]) -> list[int]:
        tot=0
        l=len(enc)+1
        x=0
        ans=[0]*l
        for i in range(1,l+1):
            tot^=i
        j=1
        while(j<len(enc)):
            x^=enc[j]
            j+=2
        ans[0]=tot^x
        for i in range(1,l):
            ans[i]=ans[i-1]^enc[i-1]
        return ans