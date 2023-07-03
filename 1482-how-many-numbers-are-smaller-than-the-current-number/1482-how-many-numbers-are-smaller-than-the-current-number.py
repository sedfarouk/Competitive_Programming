class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0]*(max(nums)+1)
        ans = []
        for i in nums:
            cnt[i]+=1
        for i in nums:
            ans.append(sum(cnt[:i]))
        return ans
