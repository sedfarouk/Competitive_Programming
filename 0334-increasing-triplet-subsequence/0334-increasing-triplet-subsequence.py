class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = s = float("inf")
        
        if len(nums)<3: return False
        
        for num in nums:
            if s<num>f: return True 
            elif num <= f:
                f = num
            else:
                s = min(num, s)
                
        return False
            
                
