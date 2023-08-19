# 1481. Leetcode - Least Number Of Unique Integers After K Removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = Counter(arr)
        vals = list(hashmap.items())
        vals.sort(key=lambda x:x[1])
        ptr = 0

        while k > 0 and ptr < len(vals):
            if vals[ptr][1]==0:
                ptr+=1
                continue
            if k >= vals[ptr][1]:
                hashmap[vals[ptr][0]]=0
                k = k - vals[ptr][1]
                ptr+=1
            elif k < vals[ptr][1]:
                break
  
        return len(list(filter(lambda x:x>0, hashmap.values())))

            
