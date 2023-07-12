class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = int(len(piles)/3)
        ans = 0
        cnt = 0
        for i in range(len(piles)-2,0,-2):
            ans+=piles[i]
            cnt+=1
            if cnt==l:
                return ans
            
