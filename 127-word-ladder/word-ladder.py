class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbours = defaultdict(list)

        for word in wordList:
            l = len(word)
            for i in range(l):
                pat = word[:i] + '*' + word[i+1:]
                neighbours[pat].append(word)

        queue = deque([(beginWord, 1)])
        vis = set()
        while queue:
            word, cnt = queue.popleft()

            if endWord == word:
                return cnt

            l = len(word)
            for i in range(l):
                pat = word[:i] + '*' + word[i+1:]

                if pat in vis: 
                    continue

                for nei in neighbours[pat]:
                    if nei not in vis:
                        queue.append((nei, cnt + 1))
                vis.add(pat)

        return 0
