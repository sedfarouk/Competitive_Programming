class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # self.pf_sum = [0]

        # for i in range(len(self.nums)):
        #     self.pf_sum.append(self.pf_sum[-1] + self.nums[i])

        self.pf_sum = [0] * (len(self.nums))
        self.pf_sum[0] = self.nums[0]

        for i in range(1, len(self.pf_sum)):
            self.pf_sum[i] = self.pf_sum[i-1] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        #return self.pf_sum[right+1] - self.pf_sum[left]
        if left==0:
            return self.pf_sum[right]
        return self.pf_sum[right] - self.pf_sum[left-1]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)