class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = countt = odd = left = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
                countt = 0
                
            while odd == k:
                if nums[left] % 2 == 1:
                    odd -= 1
                countt += 1
                left += 1
            result += countt
        
        return result
            
