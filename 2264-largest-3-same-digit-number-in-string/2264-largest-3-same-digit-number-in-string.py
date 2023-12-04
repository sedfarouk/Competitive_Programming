class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxx = float("-inf")

        for i in range(2, len(num)):
            if num[i]==num[i-1]==num[i-2]:    
                s_num = int(num[i-2:i+1])
                maxx = max(maxx, s_num)

        if maxx==float("-inf"):
            return ""

        maxx = str(maxx)
        if len(maxx) < 3:
            maxx = "0"*(3-len(maxx)) + maxx

        return maxx
        