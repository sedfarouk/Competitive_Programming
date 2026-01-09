class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * (max(nums2) + 1)
        monoStack = []

        for num in nums2:
            while monoStack and monoStack[-1] < num:
                nextGreater[monoStack.pop()] = num
            monoStack.append(num)

        return [nextGreater[num] for num in nums1]