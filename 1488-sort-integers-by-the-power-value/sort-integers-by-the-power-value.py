class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache        
        def findPower(x):
            if x == 1:
                return 0

            if x % 2:
                return findPower(x * 3 + 1) + 1
            return findPower(x // 2) + 1

        heap = []
        for i in range(lo, hi + 1):
            power = findPower(i)

            if len(heap) < k:
                heappush(heap, (-power, -i))

            elif -heap[0][0] > power:
                heapreplace(heap, (-power, -i))

        return -heap[0][1]