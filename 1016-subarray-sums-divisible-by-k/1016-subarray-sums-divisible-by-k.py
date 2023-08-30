class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        ans, cnt =  0, 0

        for i in range(len(nums)):
            cnt+=nums[i]

            ans += hashmap[cnt % k]
            hashmap[cnt % k] += 1
        return ans

            