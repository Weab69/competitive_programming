class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        
        while l<r:
            cs=numbers[l]+numbers[r]
            if cs<target:
                l+=1
            elif cs>target:
                r-=1
            else:
                return [l+1,r+1]
                 
        
        