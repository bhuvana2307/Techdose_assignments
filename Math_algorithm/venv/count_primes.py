class Solution:
    def countPrimes(self, n: int) -> int:
        l=[]
        m=math.sqrt(n)
        mc=int(m)
        c=0
        if(n<=2):
            return 0
        if(n==3):
            return 1
        if(n>3):
            for i in range(0,n):
                l.append(True)

            for i in range(2,mc+1):
                if(l[i]==True):
                    j=i*i
                    while(j<n):
                        l[j]=False
                        j+=i
            c=l.count(True)
            return c-2