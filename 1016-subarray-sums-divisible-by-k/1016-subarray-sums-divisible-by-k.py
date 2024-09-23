class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        ans = 0
        cnt = 0
        
        for num in nums:
            cnt += num
            ans += hashmap[cnt % k]
            hashmap[cnt % k] += 1
        
        return ans
            