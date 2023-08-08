# 1324. LeetCode - Print Words Vertically

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        ans = []
        max_l = 0

        for i in range(len(words)):
            max_l = max(max_l, len(words[i]))
            words[i] = [j for j in words[i]]
        
        i, x = 0, 0
        while x < max_l:
            word = ""
            for j in range(len(words)):
                if x < len(words[j]):
                    word+=words[j][x]
                else:
                    word+=" "
            x+=1
            ans.append(word.rstrip())

        return ans
