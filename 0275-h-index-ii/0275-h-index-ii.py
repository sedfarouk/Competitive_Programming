class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = -1, len(citations)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if citations[mid] >= len(citations)-mid:
                right = mid
            else:
                left = mid
        return len(citations) - right