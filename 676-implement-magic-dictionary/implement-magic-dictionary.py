class MagicDictionary:

    def __init__(self):
        self.dic = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dic.append(word)

    def search(self, searchWord: str) -> bool:
        for w in self.dic:
            if len(w) != len(searchWord):
                continue

            cnt = 0
            for i in range(len(searchWord)):
                cnt += int(searchWord[i] != w[i])

            if cnt == 1:
                return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)