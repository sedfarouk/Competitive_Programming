class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        unique = set(words[0])
        count={}

        for i in range(1, len(words)):
            unique.intersection_update(set(words[i]))

        ans = ''
        letters = list(unique)
        min_num = 0

        for ch in letters:
            num = []
            for word in words:
                num.append(word.count(ch))
            ans+=ch*min(num)

        return list(ans)