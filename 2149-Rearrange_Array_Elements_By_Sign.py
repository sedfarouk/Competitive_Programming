# 2149. LeetCode - Rearrange Array Elements By Sign 

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Faster than 2 pointer approach. Using zip function
        ans = []
        neg, pos = [i for i in nums if i < 0], [i for i in nums if i > -1]

        temp = zip(pos, neg)

        for i in temp:
            ans.append(i[0])
            ans.append(i[1])

        return ans

        # Two Pointer Approach 
        # i = 0
        # neg_ptr, pos_ptr = 0, 0
        # while i < len(nums) and pos_ptr < len(nums) and neg_ptr < len(nums):
        #     if i%2==0:
        #         ans.append(pos[pos_ptr])
        #         pos_ptr+=1
        #     else:
        #         ans.append(neg[neg_ptr])
        #         neg_ptr+=1
        #     i+=1
        # ans.extend(neg[neg_ptr+1:])
        # ans.extend(pos[pos_ptr+1:])

        # return ans
