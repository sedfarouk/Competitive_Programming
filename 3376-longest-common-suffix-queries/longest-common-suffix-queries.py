class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = 0
        self.len = 1e4

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word, idx):
        curr = self.root
        n = len(word)

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if n < curr.len: 
                curr.idx = idx
                curr.len = n
    
    def searchSuff(self, word):
        curr = self.root
        ans = curr.idx
        for ch in word:
            if ch not in curr.children:
                return ans
            curr = curr.children[ch]
            ans = curr.idx
        return ans

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        res = []

        for idx, word in enumerate(wordsContainer):
            trie.addWord('/' + word[::-1], idx)
        
        for word in wordsQuery:
            res.append(trie.searchSuff('/' + word[::-1]))

        return res