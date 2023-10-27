class Solution:
    def climbStairs(self, n: int) -> int:
        f,s=1,1
        
        for i in range(n-1):
            temp=f
            f=f+s
            s=temp
        return f
         