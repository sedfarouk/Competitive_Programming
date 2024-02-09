class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)
        
        for num in nums:
            if hashmap[num-1]:
                heappush(hashmap[num], heappop(hashmap[num-1])+1)
            else:
                heappush(hashmap[num], 1)

        for k, n in hashmap.items():
            if hashmap[k]:
                l = heappop(hashmap[k])
                if l < 3:
                    return False
        return True
            
        