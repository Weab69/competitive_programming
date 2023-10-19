class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        o=[intervals[0]]
        for start,end in intervals[1:]:
            lastEnd=o[-1][1]
            if start<=lastEnd:
                o[-1][1]=max(lastEnd,end)
            else:
                o.append([start,end] )
        return o        
            
          