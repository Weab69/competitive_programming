class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        c=0
        l=0
        r=len(piles)-2
        while l<r:
            c+=piles[r]  
            l+=1
            r-=2
        return c           
                   