class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            asc = ord(ch) - 97
            if not curr.children[asc]:
                curr.children[asc] = TrieNode()
            curr = curr.children[asc]
        curr.is_end = True

    def search(self, word: str, s=True) -> bool:
        curr = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.is_end if s else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, False)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)