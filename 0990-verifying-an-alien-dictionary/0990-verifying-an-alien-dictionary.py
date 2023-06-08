class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_index = dict()
        for index, c in enumerate(order):
            char_to_index[c] = index
        for j in range(1, len(words)):
            curr = len(words[j])
            prev = len(words[j-1])
            p, q = 0, 0
            while p < curr and q < prev:
                if char_to_index[words[j][p]] < char_to_index[words[j-1][q]]:
                    return False
                if char_to_index[words[j][p]] > char_to_index[words[j-1][q]]:
                    break
                p+=1
                q+=1
            if p == curr and q < prev:
                return False        
        return True


