class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxx = ""

        for i in range(2, len(num)):
            if num[i]==num[i-1]==num[i-2]:    
                maxx = max(maxx, num[i-2:i+1])
                
        return maxx
        