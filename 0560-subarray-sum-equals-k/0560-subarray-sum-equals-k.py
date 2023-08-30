class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = 0

        hashmap = defaultdict(int)
        hashmap[0] = 1

        for i in range(len(nums)):
            cnt+=nums[i]

            if (cnt-k) in hashmap.keys():
                ans+=hashmap[cnt-k]

            hashmap[cnt] += 1

        return ans
