class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        if k % 5 == 0 or k % 2 == 0: return -1

        rem = 0
        for i in range(1, k + 1):
            rem = (rem * 10) + 1
            if rem % k == 0: return i

        return -1 


        
        