# LeetCode 179 - Largest Number

class LargerNum(str):
    def __lt__(a, b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNum)
        ans = ''.join(nums)

        if ans[0]=="0":
            return "0"
        return ans

        
