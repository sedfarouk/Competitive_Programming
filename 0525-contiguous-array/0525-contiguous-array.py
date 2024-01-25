class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxx = 0
        hashmap = defaultdict(int)
        hashmap[0] = 0
        pref = 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                pref -= 1
            else:
                pref += 1
                
            if pref in hashmap:
                maxx = max(maxx, i - hashmap[pref] + 1)
            else:
                hashmap[pref] = i + 1
                
        return maxx
            
            