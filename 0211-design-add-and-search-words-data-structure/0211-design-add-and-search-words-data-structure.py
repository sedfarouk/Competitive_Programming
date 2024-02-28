class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def dfs(self, curr, idx, word):
        if idx==len(word):
            return curr.is_end

        if word[idx]!='.':
            if word[idx] in curr.children and self.dfs(curr.children[word[idx]], idx+1, word):
                return True
        else:
            for c in curr.children.keys():
                if self.dfs(curr.children[c], idx+1, word):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)