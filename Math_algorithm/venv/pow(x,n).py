class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        if(n>0):
            while(n>0):
                if(n%2==1):
                    res*=x
                x=x*x
                n//=2
        else:
            if n==0:
                return 1
            pos=abs(n)
            while(pos>0):
                if(pos%2==1):
                    res*=x
                x=x*x
                pos//=2
            res=1/res
        return res