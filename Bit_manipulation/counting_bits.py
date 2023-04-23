class Solution:
    def countBits(self, n: int) -> list[int]:
        l=[]
        l.append(0)
        for i in range(1,n+1):
            c=0
            while(i>0):
                if(i%2==1):
                    c+=1
                i//=2
            l.append(c)
        return l