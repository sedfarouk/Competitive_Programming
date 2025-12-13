class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Element:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for idx, product in enumerate(products):
            self.addWord(product)

        ans = []
        for ch in searchWord:
            if ans and not ans[-1]:
                ans.append([])
            else:
                ans.append(self.search(ch))

        return ans

    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

            if len(curr.words) < 3:
                heappush(curr.words, Element(word))
            elif word < curr.words[0].word:
                heapreplace(curr.words, Element(word))

    def search(self, char):
        if char not in self.root.children:
            return []
        self.root = self.root.children[char]
        return sorted([item.word for item in self.root.words])