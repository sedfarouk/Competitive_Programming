class Solution:
    def minOperations(self, nums: List[int]) -> int:
        countt = Counter(nums)
        ans = 0

        for key, val in countt.items():
            if val==1:
                return -1

            moves = val // 3
            ans += moves + (val-(3*moves)) // 2

            if val % 3 == 1:
                ans += 1

        return ans
            
