class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        h = Counter(nums[:k - 1])
        mx = max(nums)
        ans = []

        for r in range(k - 1, n):
            h[nums[r]] += 1

            heap = []
            for i in range(mx, 0, -1):
                if len(heap) == x:
                    if h[i] > heap[0][0]:
                        heapreplace(heap, (h[i], i))
                elif h[i] > 0:
                    heappush(heap, (h[i], i))

            summ = 0
            for freq, val in heap:
                summ += val * freq
                
            ans.append(summ)
            h[nums[r - k + 1]] -= 1

        return ans



