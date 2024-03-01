class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

    def search(self, node, i, word):
        if i==len(word):
            return True
        
        if not node:
            return False

        if word[i] in node.children.keys():
            return self.search(node.children[word[i]], i+1, word)

        else:
            for c in node.children.values():
                if self.search(c, i, word):
                    return True
                    
        return False


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.addWord(s)
        ans = 0
        memo = {}

        for w in words:
            if w in memo:
                ans += memo[w]
            else:
                memo[w] = trie.search(trie.root, 0, w)
                ans += memo[w]

        return ans

        
        