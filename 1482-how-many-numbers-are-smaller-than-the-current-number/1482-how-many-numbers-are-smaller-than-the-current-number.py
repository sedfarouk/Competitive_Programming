class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            num = 0
            for j in nums:
                if j!=i and i>j:
                    num +=1
            ans.append(num)
        return ans
