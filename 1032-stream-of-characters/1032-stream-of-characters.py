class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

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

    def search(self, word):
        curr = self.root

        for ch in word:
            if curr.is_end:
                return True
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.queried_string = ""

        for w in words:
            self.trie.addWord(w[::-1])

    def query(self, letter: str) -> bool:
        if len(self.queried_string)==200:
            self.queried_string = ""
        self.queried_string += letter
        return self.trie.search(self.queried_string[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)