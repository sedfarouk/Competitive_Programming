# 985. Leetcode - Sum of even numbers after queries

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evens = sum([x for x in nums if x%2==0])

        for query in queries:
            if nums[query[1]]%2==0:
                evens -= nums[query[1]]

            nums[query[1]]+=query[0]

            if nums[query[1]]%2==0:
                evens += nums[query[1]]
                
            ans.append(evens)

        return ans
