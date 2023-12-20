class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minn1, minn2 = min(prices[:2]), max(prices[:2])
        
        for i in range(2, len(prices)):
            if prices[i] < minn1:
                minn2 = minn1
                minn1 = prices[i]
            
            else:
                minn2 = min(minn2, prices[i])
                
        cost = minn1+minn2    
        if cost > money:
            return money
        return money-(minn1+minn2)
        