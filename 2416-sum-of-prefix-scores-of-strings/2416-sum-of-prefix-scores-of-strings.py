class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
   
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr.children[ch].count += 1
            curr = curr.children[ch]
            
    def search(self, word):
        curr = self.root
        ans = 0
        
        for ch in word:
            ans += curr.children[ch].count
            curr = curr.children[ch]       
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for w in words:
            trie.addWord(w)
            
        ans = [0]*len(words)
        for i in range(len(words)):
            ans[i] = trie.search(words[i])
            
        return ans