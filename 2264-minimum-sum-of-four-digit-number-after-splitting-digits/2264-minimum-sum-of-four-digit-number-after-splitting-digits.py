class Solution:
    def minimumSum(self, num: int) -> int:
        lst = list(map(int, str(num)))
        lst.sort()
        return int(str(lst[0])+str(lst[2]))+int(str(lst[1])+str(lst[3]))