class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        maxx = max(nums)

        if maxx < 0:
            return 1
        
        for i in range(1, maxx+1):
            if i not in hashmap:
                return i
        return maxx+1
        


        