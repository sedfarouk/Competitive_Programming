class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(l, r, turn):
            if l > r:
                return 0
            if turn:
                return max(dp(l+1, r, False)+nums[l], dp(l, r-1, False)+nums[r])
            else:
                return min(dp(l+1, r, True)-nums[l], dp(l, r-1, True)-nums[r])
            
        return dp(0, len(nums)-1, True) >= 0