class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pref = [0]

        for num in nums:
            pref.append(pref[-1] + num)

        ans = 0
        for i in range(len(nums)):
            if not nums[i]:
                ans += 0 <= (pref[i + 1] - (pref[-1] - pref[i])) <= 1
                ans += -1 <= (pref[i + 1] - (pref[-1] - pref[i])) <= 0

        return ans