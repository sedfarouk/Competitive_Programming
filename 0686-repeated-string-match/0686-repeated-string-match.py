class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        def func(repeat):
            val = b + '#' + a*repeat

            lps = [0]*len(val)

            for i in range(1, len(val)):
                j = lps[i-1]

                while j > 0 and val[i]!= val[j]:
                    j = lps[j-1]

                if val[i] == val[j]:
                    j +=1

                if j == len(b):
                    return 1

                lps[i] = j

            return 0

        for i in range(len(b)//len(a), len(b)//len(a)+3):
            if func(i): return i
        return -1

        