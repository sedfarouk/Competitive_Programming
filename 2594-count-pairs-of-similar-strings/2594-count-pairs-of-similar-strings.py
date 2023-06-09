class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if set(words[i]).difference(words[j]) == set() and set(words[j]).difference(words[i]) == set():
                    count+=1
        return count
    