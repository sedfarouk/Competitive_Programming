class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        
        for i in range(len(arr)):
            if arr[i]-ans>0:
                ans += 1
        return ans
            
        
