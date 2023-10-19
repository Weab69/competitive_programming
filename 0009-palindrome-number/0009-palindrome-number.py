class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
          return False
        d=1
        while x>=d*10:
            d*=10
        while x:
            r=x%10
            l=x//d
            if r!=l:
                return False
            x=(x%d)//10
            d=d/100
        return   True  
            