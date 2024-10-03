class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        minn = len(nums)
        rem = sum(nums) % p

        if rem==0:
            return 0

        hashmap = defaultdict(int)
        hashmap[0] = -1
        curr = 0

        for i in range(len(nums)):
            curr = (curr + nums[i]) % p
            hashmap[curr] = i

            if (curr-rem) % p in hashmap:
                minn = min(minn, i - hashmap[(curr-rem) % p])

        return minn if minn != len(nums) else -1

        
