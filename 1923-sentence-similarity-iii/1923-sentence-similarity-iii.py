class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        
        if sentence1 == sentence2[:len(sentence1)] or sentence1 == sentence2[::-1][:len(sentence1)][::-1]:
            return True

        if sentence2 == sentence1[:len(sentence2)] or sentence2 == sentence1[::-1][:len(sentence2)][::-1]:
            return True

        def add(s):
            res = defaultdict(list)

            for idx, word in enumerate(s[::-1]):
                res[word].append(len(s)-idx-1)
            return res

        s1 = add(sentence1)
        s2 = add(sentence2)

        i = j = 0
        used = False
        while i < len(sentence1) and j < len(sentence2):
            if sentence1[i]==sentence2[j]:
                s1[sentence1[i]].pop()
                s2[sentence2[j]].pop()
                i += 1; j += 1
            else:
                if used or (sentence2[j] not in s1 and sentence1[i] not in s2):
                    return False

                used = True
                if s2[sentence1[i]]:
                    last = sentence1[i]
                    j = s2[sentence1[i]].pop() + 1
                    i = s1[sentence1[i]].pop() + 1

                    while i==len(sentence1) and j < len(sentence2) and sentence2[j]==last:
                        j = s2[last].pop() + 1

                elif s1[sentence2[j]]:
                    last = sentence2[j]
                    i = s1[sentence2[j]].pop() + 1
                    j = s2[sentence2[j]].pop() + 1

                    while j==len(sentence2) and i < len(sentence1) and sentence1[i]==last:
                        i = s1[last].pop() + 1

        if used and (i != len(sentence1) or j != len(sentence2)):
            return False
        return True
