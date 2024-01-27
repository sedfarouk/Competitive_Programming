class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        monostack = deque()
        minimums = [0] * n
        
        for i in range(1, n):
            if nums[i] < nums[minimums[i-1]]:
                minimums[i] = i
            else:
                minimums[i] = minimums[i-1]
        
        for i in range(n):
            while monostack and nums[monostack[-1]] <= nums[i]:
                monostack.pop()
                
            if monostack and nums[minimums[monostack[-1]]] < nums[i]:
                return True
             
            monostack.append(i)                      
        return False
        
        
        