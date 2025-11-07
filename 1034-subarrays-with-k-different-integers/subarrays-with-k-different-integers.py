class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def sliding_window(x):
            ans = l = 0
            h = defaultdict(int)

            for r in range(n):
                h[nums[r]] += 1

                while len(h) > x:
                    h[nums[l]] -= 1

                    if not h[nums[l]]:
                        del h[nums[l]]
                    l += 1
                ans += r - l + 1
            return ans
        
        return sliding_window(k) - sliding_window(k - 1)

        
