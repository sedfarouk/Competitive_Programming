class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        mid = len(nums)//2
        for i in range(mid):
            arr.append(nums[i])
            arr.append(nums[mid+i])

        return arr