class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def findPower(x):
            steps = 0
            while x != 1:
                if x % 2: x = x * 3 + 1
                else: x //= 2
                steps += 1
            return steps

        heap = []
        for i in range(lo, hi + 1):
            power = findPower(i)

            if len(heap) < k:
                heappush(heap, (-power, -i))

            elif -heap[0][0] > power:
                heapreplace(heap, (-power, -i))

        return -heap[0][1]