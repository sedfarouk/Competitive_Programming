class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        built = True

        for idx, ch in enumerate(word):
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

                if idx != len(word) - 1:
                    built = False 

            curr = curr.children[ch]
            
            if idx != len(word) - 1:
                built &= curr.end

        curr.end = True
        return word if built else ""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res = ""
        trie = Trie()

        for word in words:
            w = trie.addWord(word)

            if len(w) >= len(res):
                if len(w) == len(res) and w < res:
                    res = w
                elif len(w) > len(res):
                    res = w

        return res