class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []

        for query in queries:
            add = True
            j = 0
            for i in range(len(query)):
                if j < len(pattern) and query[i]==pattern[j]:
                    j += 1
                elif query[i].isupper():
                    add = False

            if add and j==len(pattern):
                ans.append(True)
            else:
                ans.append(False)

        return ans