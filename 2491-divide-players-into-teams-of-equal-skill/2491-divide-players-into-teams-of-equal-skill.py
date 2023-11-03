class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        t=skill[0]+skill[-1]
        l,r=0,len(skill)-1
        ans=0
        
        while l<r:
            if skill[l]+skill[r]!=t:
                return -1
            ans+=skill[l]*skill[r]
            l,r=l+1,r-1
        return ans