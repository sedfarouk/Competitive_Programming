class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        win_sum, tmp = 0, 0
        hashmap = defaultdict(int)

        for right in range(len(nums)):
            tmp += nums[right]
            hashmap[nums[right]]+=1

            if right >= k-1:
                if len(hashmap.keys())==k:
                    win_sum = max(win_sum, tmp)
                if hashmap.get(nums[left]) > 1:
                    hashmap[nums[left]]-=1
                else:
                    del hashmap[nums[left]]
                tmp-=nums[left]
                left+=1                                

        return win_sum
