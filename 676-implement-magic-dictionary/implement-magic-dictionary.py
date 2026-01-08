class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word):
        n = len(word)
        
        def dfs(i, c, node):
            if i == n:
                return c == 1 and node.end

            for ch in node.children:
                if ch == word[i] and dfs(i + 1, c, node.children[ch]):
                    return True
                elif ch != word[i] and not c and dfs(i + 1, 1, node.children[ch]):
                    return True 
            return False
        return dfs(0, 0, self.root)                             
        

class MagicDictionary:

    def __init__(self):
        self.dic = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dic.addWord(word)

    def search(self, searchWord: str) -> bool:
        return self.dic.search(searchWord)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)