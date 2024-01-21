class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        heap = [(-freq, key) for key, freq in hashmap.items()]
        heapify(heap)
        ans = removed = 0

        while heap:
            freq, key = heappop(heap)
            removed += freq * -1
            ans += 1

            if len(arr) - removed <= len(arr) // 2:
                return ans


