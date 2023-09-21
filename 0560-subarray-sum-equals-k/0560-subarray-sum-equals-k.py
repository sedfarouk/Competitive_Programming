class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
            
        hashmap = defaultdict(int)
        hashmap[0] = 1
        ans = 0        

        for i in range(len(nums)):
            ans += hashmap[prefix_sum[i+1]-k]
            hashmap[prefix_sum[i+1]] += 1
        
        return ans