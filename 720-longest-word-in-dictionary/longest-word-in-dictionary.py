class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                return ""

            curr = curr.children[ch]

            if not curr.end:
                return ""
        
        return word 


class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ""
        trie = Trie()

        for word in words:
            trie.addWord(word)

        for word in words:
            w = trie.search(word)

            if len(w) >= len(res):
                if len(w) == len(res) and w < res:
                    res = w
                elif len(w) > len(res):
                    res = w

        return res