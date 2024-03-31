class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        hashmap = {0:-1}
        ans = len(nums)
        pref_sum = 0

        for idx, num in enumerate(nums):
            pref_sum += num
            rem = pref_sum % p
            hashmap[rem] = idx
    
            if (rem-need)%p in hashmap:
                ans = min(ans, idx-hashmap[(rem-need)%p])        
        
        return ans if ans<len(nums) else -1