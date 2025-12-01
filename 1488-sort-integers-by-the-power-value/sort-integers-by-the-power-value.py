class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}        
        def findPower(x):
            if x in memo:
                return memo[x]

            if x == 1:
                return 0

            if x % 2:
                memo[x] =  findPower(x * 3 + 1) + 1
            else:
                memo[x] = findPower(x // 2) + 1
            return memo[x]

        heap = []
        for i in range(lo, hi + 1):
            power = findPower(i)

            if len(heap) < k:
                heappush(heap, (-power, -i))

            elif -heap[0][0] > power:
                heapreplace(heap, (-power, -i))

        return -heap[0][1]