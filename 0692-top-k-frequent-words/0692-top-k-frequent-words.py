class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_freq = Counter(words)
        
        heap = []
        for key, val in words_freq.items():
            heap.append((-val, key))
            
        heapify(heap)
        
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
            
        return ans

        

        
        
