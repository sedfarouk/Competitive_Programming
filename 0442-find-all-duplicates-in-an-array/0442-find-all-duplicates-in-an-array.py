class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
#         ans = []
#         hashmap = Counter(nums)

#         for i in hashmap.keys():
#             if hashmap[i] > 1:
#                 ans.append(i)
#         return ans

        ans = []
        i = 0
        n = len(nums)
        
        while i < n:
            correctIdx = nums[i]
            if nums[i] != nums[correctIdx-1]:
                nums[i], nums[correctIdx-1] = nums[correctIdx-1], nums[i]
                
            else:
                i += 1
                
        for j in range(n):
            if j != nums[j]-1:
                ans.append(nums[j])
                
        return ans
