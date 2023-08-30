class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # BRUTE FORCE
        # ans = []

        # for i in range(len(nums)):
        #     left, right = 1, 1

        #     for j in range(i):
        #         left*=nums[j]
            
        #     for j in range(i+1, len(nums)):
        #         right*=nums[j]

        #     ans.append(left*right)

        ans = []

        prefix_prod = [1]
        suffix_prod = [1]

        for i in range(len(nums)):
            prefix_prod.append(prefix_prod[-1]*nums[i])

        for i in range(len(nums)-1, -1, -1):
            suffix_prod.append(suffix_prod[-1]*nums[i])

        suffix_prod.reverse()

        i = 0
        while i < len(suffix_prod) -1:
            ans.append(prefix_prod[i]*suffix_prod[i+1])
            i+=1

        return ans

