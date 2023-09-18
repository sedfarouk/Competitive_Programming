class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all_in_H_hours(mid):
            time  = 0

            for i in range(len(piles)):
                time += ceil(piles[i] / mid)
            
            if time <= h:
                return True
            return False

        left, right = 1, max(piles)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2

            if can_eat_all_in_H_hours(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans