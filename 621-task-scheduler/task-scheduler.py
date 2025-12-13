class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreqs = Counter(tasks)
        ss = [(-f, k) for k, f in taskFreqs.items()]
        heapify(ss)
        res = 0
        
        while ss:            
            if -ss[0][0] == 1:
                res += len(ss)
                break
            
            res += n + 1

            processed = []
            for _ in range(min(len(ss), n + 1)):
                f, k = heappop(ss)
                processed.append((f, k))
                    
            for f, k in processed:
                if f + 1 < 0:
                    heappush(ss, (f + 1, k))
                    
        return res