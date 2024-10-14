class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = [-x for x in nums]
        heapify(nums)

        while k:
            x = heappop(nums)*-1
            heappush(nums, -ceil(x/3))
            ans += x
            k -= 1
        return ans

        