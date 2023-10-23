class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        carSet=set()
        l,res=0,0
        
        for r in range(len(s)):
            while s[r] in carSet:
                carSet.remove(s[l])
                l+=1
            carSet.add(s[r])
            res=max(res,r-l+1)
        return res
         