class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        h = defaultdict(int)

        for num in nums[:k]:
            heappush(heap, -num)
            h[num] += 1
        
        ans = [-heap[0]]
        for i in range(k, len(nums)):
            h[nums[i-k]] -= 1
            if h[nums[i-k]]==0:
                del h[nums[i-k]]

            h[nums[i]] += 1
            heappush(heap, -nums[i])

            while -heap[0] not in h:
                heappop(heap)
            
            ans.append(-heap[0])
        
        return ans
            
            

