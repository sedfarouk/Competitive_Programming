class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        solution = []

        for w in words:
            trie.addWord(w)

        m, n = len(board), len(board[0])
        def inbounds(i, j):
            return 0<=i<m and 0<=j<n

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c, cur):
            if not inbounds(r, c) or board[r][c] not in cur.children: 
                return

            original_char = board[r][c]
            cur = cur.children[original_char]
            board[r][c] = '#'

            if cur.word!=None:
                solution.append(cur.word)
                cur.word = None

            for x, y in dirs: 
                dfs(r + x, c + y, cur)
            board[r][c] = original_char

        for r in range(m):
            for c in range(n):
                dfs(r, c, trie.root)
        return solution
            
