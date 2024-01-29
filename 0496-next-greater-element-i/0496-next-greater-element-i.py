class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        monoStack = deque()
        hashMap = defaultdict(int)

        for num in nums2:
            hashMap[num] = -1

        for i in range(n):
            while monoStack and nums2[monoStack[-1]] <= nums2[i]:
                hashMap[nums2[monoStack.pop()]] = nums2[i]
            monoStack.append(i)

        ans = []
        for num in nums1:
            ans.append(hashMap[num])

        return ans



