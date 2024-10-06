class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        
        f1, s1 = 0, len(sentence1)-1
        f2, s2 = 0, len(sentence2)-1

        if sentence1==sentence2[:s1+1] or sentence1==sentence2[-s1:]:
            return True

        while f1 <= s1 and f2 <= s2:
            if sentence1[f1]==sentence2[f2]:
                f1 += 1; f2 += 1
            elif sentence1[s1]==sentence2[s2]:
                s1 -= 1; s2 -= 1
            else:
                return False
        return f1 > s1 or f2 > s2
