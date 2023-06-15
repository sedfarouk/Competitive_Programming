class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1: 
            return 1
        return (k + self.findTheWinner(n-1, k) -1) % n + 1