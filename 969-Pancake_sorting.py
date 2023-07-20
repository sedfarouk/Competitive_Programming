# 969. Leetcode - Pancake sorting

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        curr = len(arr)-1
        
        # Make maximum move to beginning then to the end
        while curr > 0:
            if sorted(arr) == arr:
                return ans
            max_num = max(arr[:curr+1])
            ans.append(arr.index(max_num)+1)
            arr[:arr.index(max_num)+1] = reversed(arr[:arr.index(max_num)+1])
            arr[:curr+1] = reversed(arr[:curr+1])
            ans.append(curr+1)
            curr-=1
        
        return ans
        
