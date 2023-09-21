class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = 1, sum(weights)

        def least_capacity(mid, days):
            carried, time = 0, 0
            
            for weight in weights:
                carried += weight

                if weight > mid:
                    return False
                if carried > mid:
                    time += 1
                    carried = weight
                if carried == mid:
                    time += 1
                    carried = 0
            
            if carried > 0:
                time += 1

            if time <= days:
                return True
            return False

        while left + 1 < right:
            mid = left + (right - left) // 2

            if least_capacity(mid, days):
                right = mid
            else:
                left = mid

        return right
            
        
        