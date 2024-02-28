class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            idx = ord(ch)-97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def dfs(self, curr, idx, word):
        if idx==len(word):
            return curr.is_end

        id = ord(word[idx])-97
        if word[idx]!='.':
            if curr.children[id] and self.dfs(curr.children[id], idx+1, word):
                return True
        else:
            for id in range(26):
                if curr.children[id] and self.dfs(curr.children[id], idx+1, word):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)