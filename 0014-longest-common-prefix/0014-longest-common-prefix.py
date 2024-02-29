class TrieNode:
    def __init__(self):
        self.is_end = False
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
        curr.is_end = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_word = ""

        for w in strs:
            if len(w) > len(longest_word):
                longest_word = w

        root = Trie()
        root.addWord(longest_word)
        r = root.root

        def dfs(node, idx, word):
            if idx==len(word): return ""
            if word[idx] not in node.children: return ""
            
            return word[idx] + dfs(node.children[word[idx]], idx+1, word)

        common_prefix = "#"*200
        for w in strs:
            if w!=longest_word:
                prefix = dfs(r, 0, w)
                if len(prefix) < len(common_prefix):
                    common_prefix = prefix
        return common_prefix if common_prefix!="#"*200 else longest_word

        

