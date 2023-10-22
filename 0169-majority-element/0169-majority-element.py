class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        co={}
        res,maxCo=0,0
        
        for n in nums:
            co[n]=1+co.get(n,0)
            res= n if co[n]>maxCo else res
            maxCo=max(co[n],maxCo)
        return res
        