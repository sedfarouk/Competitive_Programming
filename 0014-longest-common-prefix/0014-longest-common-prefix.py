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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_word = ""

        for w in strs:
            if len(w) > len(longest_word):
                longest_word = w

        myTrie = Trie()
        myTrie.addWord(longest_word)

        def dfs(node, idx, word):
            if idx==len(word): return 0
            if word[idx] not in node: return 0
            
            return dfs(node[word[idx]], idx+1, word) + 1

        common_length = float("inf")
        for w in strs:
            common_length = min(common_length, dfs(myTrie.root, 0, w))
        return strs[0][:common_length]

        

