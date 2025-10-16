class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = Counter([num % value for num in nums])
        cnt = 0

        while True:
            if not mods[cnt % value]:
                return cnt
            mods[cnt % value] -= 1
            cnt += 1




        