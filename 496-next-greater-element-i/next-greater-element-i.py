class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = defaultdict(lambda: -1)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                nextGreater[stack.pop()] = nums2[i]

            stack.append(nums2[i])

        return [nextGreater[x] for x in nums1]
