class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        ans = 0

        for w in wordList:
            n = len(w)
            for i in range(n):
                graph[w[:i] + '*' + w[i+1:]].append(w)

        queue = deque([beginWord])
        vis = set([beginWord])
        while queue:
            l = len(queue)
            ans += 1

            for _ in range(l):
                w = queue.popleft()
                n = len(w)

                if w == endWord:
                    return ans

                for i in range(n):
                    for nei in graph[w[:i] + '*' + w[i+1:]]:
                        if nei not in vis:
                            queue.append(nei)
                            vis.add(nei)         
        
        return 0
