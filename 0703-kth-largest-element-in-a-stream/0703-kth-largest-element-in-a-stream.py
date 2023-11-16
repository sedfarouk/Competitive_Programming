class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums, reverse=True)[:k]
        self.heap = [num for num in nums]
        heapify(self.heap)
        self.k = k


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        minn = heapq.heappop(self.heap)

        if minn < val:
            heapq.heappush(self.heap, val)
            return self.heap[0]
    
        heapq.heappush(self.heap, minn)
        return minn


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)