# 1323. Leetcode - Maximum 69 number

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        ans = ""

        for i in range(len(num)):
            if num[i]=="6":
                return int(ans+"9"+num[i+1:])
            ans+=num[i]

        return int(ans)
