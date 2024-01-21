class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapify(heap)

        for _ in range(k):
            num = heappop(heap)
            heappush(heap, num//2)

        return -sum(heap)
