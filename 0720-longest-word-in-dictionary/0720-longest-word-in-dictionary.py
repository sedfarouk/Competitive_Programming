class Trie:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch] 


class Solution:
    def longestWord(self, words: List[str]) -> str:
        myTrie = Trie()
        sett = set(words)

        for w in words:
            myTrie.addWord(w)

        queue = deque([(v, k) for k, v in myTrie.root.items()])
        maxx_str = ""

        while queue:
            level = len(queue)

            for _ in range(level):
                q, s = queue.popleft()
                
                for k, v in q.items():
                    if s in sett: 
                        queue.append((v, s+k))

                if s in sett and (len(s) > len(maxx_str) or (len(s)==len(maxx_str) and maxx_str > s)):
                    maxx_str = s
        return maxx_str


        