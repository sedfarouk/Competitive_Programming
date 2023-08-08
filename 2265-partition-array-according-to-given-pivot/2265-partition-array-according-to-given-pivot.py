class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [i for i in nums if i < pivot] + [i for i in nums if i==pivot] + [i for i in nums if i > pivot]