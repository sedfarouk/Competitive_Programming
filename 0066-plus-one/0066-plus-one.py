class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = int("".join([str(i) for i in digits]))
        ans = str(ans + 1)
        return [int(i) for i in ans]


        