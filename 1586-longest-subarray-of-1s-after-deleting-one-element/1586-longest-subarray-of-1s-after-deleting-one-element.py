class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # m=dict()
        l=[]
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                # m[i]=c
                l.append(c)
                c=0
            else:
                c+=1
        l.append(c)
        a=0
        if len(l)==1:
            return l[0]-1
        # print(l)
        for i in range(len(l)-1):
            a=max(a,l[i]+l[i+1])

        return a

        # window = []
        # left, cnt, ans = 0, 0, 0

        # for right in range(len(nums)):
        #     window = nums[left:right+1]

        #     if nums[right]==0:
        #         cnt+=1

        #     while cnt > 1:
        #         if nums[left]==0:
        #             cnt-=1
        #         left+=1

        #     ans = max(ans, right-left)

        # return ans