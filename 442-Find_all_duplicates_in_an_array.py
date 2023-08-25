# 442. Leetcode - Find all duplicates in an array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        hashmap = Counter(nums)

        for i in hashmap.keys():
            if hashmap[i] > 1:
                ans.append(i)
        return ans
