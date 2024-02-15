class Solution:
    def countBits(self, n: int) -> List[int]:       
        ans = []
        for dig in range(n+1):
            rem = 0
            while dig>0:
                rem += dig%2
                dig //= 2
            ans.append(rem)
        return ans