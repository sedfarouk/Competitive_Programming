class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappush(heap, nums[i])
            heapq.heappop(heap)

        return heapq.heappop(heap)


        # heap = [-num for num in nums]
        # heapify(heap)
        # cnt = 0

        # while cnt < k - 1:
        #     heapq.heappop(heap)
        #     cnt += 1
        # val = heapq.heappop(heap)
        # if val > 0:
        #     return -val
        # return abs(val)


        