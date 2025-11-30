class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cnt = 0

    def add(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def searchMagic(self, word):
        def dfs(root, i):
            if i == len(word):
                return self.cnt == 1 and root.end

            for ch in root.children:
                self.cnt += int(word[i] != ch)

                if self.cnt < 2 and dfs(root.children[ch], i + 1):
                    self.cnt = 0
                    return True

                self.cnt -= int(word[i] != ch)

            return False

        return dfs(self.root, 0)

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.add(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.searchMagic(searchWord)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)