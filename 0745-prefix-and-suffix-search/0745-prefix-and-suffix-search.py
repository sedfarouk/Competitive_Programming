class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word, idx):
        curr_node = self.root

        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
                curr_node.index = idx
            curr_node = curr_node.children[ch]
            curr_node.index = idx
        
    def search(self, query):
        curr_node = self.root

        for ch in query:
            if ch not in curr_node.children:
                return -1
            curr_node = curr_node.children[ch]
        return curr_node.index


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for idx, w in enumerate(words):
            for i in range(len(w)):
                self.trie.addWord(w[i:]+'#'+w, idx)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(suff+'#'+pref)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)