class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        limits = defaultdict(set)
        parents = defaultdict(int)
        ans = []

        for x, y in queries:
            if x not in limits[y]:
                limits[y].add(x)
                if x in parents:
                    limits[parents[x]].remove(x)
                    if not limits[parents[x]]:
                        del limits[parents[x]]

                parents[x] = y
            ans.append(len(limits))

        return ans