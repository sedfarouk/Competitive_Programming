class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num==2:
                ans.append(-1)
            else:
                b = bin(num)[2:]
                x = ""
                for i in range(len(b)):
                    if b[i] == "0":
                        x = b[:i+1] + "0" + b[i+2:]
                
                if x:
                    ans.append(int(x, 2))
                else:
                    ans.append(int("0"+b[1:], 2))
        return ans