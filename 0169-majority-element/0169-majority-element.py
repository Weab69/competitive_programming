class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,co=0,0
        
        for n in nums:
            if co==0:
                res=n
            co+=(1 if n==res else -1)
        return res     
            
         