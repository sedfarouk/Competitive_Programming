# 2799. Leetcode - Count Complete Subarrays In An Array

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        ans = 0
        win = []

        for i in range(len(nums)):
            win = nums[:i+1]

            if len(set(win))==distinct:
                hashmap = Counter(win)
                for j in win:
                    if hashmap[j] > 1:
                        ans+=1
                        hashmap[j]-=1
                    elif hashmap[j] == 1:
                        ans+=1
                        break
                        
        return ans
        
