class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = k
        for x in nums:
            if not x:
                c += 1
            else:
                if c < k: return False
                c = 0
        return True

