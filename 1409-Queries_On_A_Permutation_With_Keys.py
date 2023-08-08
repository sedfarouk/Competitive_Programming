# 1409. LeetCode - Queries On A Permutation With Keys

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        pos = [i for i in range(1, m+1)]
        ans = []

        for i in queries:
            idx = pos.index(i)
            ans.append(idx)
            pos.pop(idx)
            pos.insert(0,i)
            
        return ans
