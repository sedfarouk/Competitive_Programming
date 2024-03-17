class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        
        i = 0
        while i < n and intervals[i][1] < new[0]:
            ans.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= new[1]:
            new[0] = min(new[0], intervals[i][0])
            new[1] = max(new[1], intervals[i][1])
            i += 1
            
        ans.append(new)
        
        while i < n:
            ans.append(intervals[i])
            i += 1
        
        return ans
            
        