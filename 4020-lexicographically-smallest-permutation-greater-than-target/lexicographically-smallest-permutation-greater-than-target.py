class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        prefTarget = [[0] * 26]
        freqS = [0] * 26

        for i in range(n):
            prefTarget.append(prefTarget[-1][:])
            prefTarget[-1][ord(target[i]) - 97] += 1

            freqS[ord(s[i]) - 97] += 1
 
        for i in range(n - 1, -1, -1):
            ok = True
            freq = freqS[:]

            for j in range(26):
                if prefTarget[i][j] > freq[j]:
                    ok = False
                freq[j] -= prefTarget[i][j]

            if not ok: continue

            gtChar = ''
            for j in range(ord(target[i]) - 96, 26):
                if freq[j]:
                    gtChar = chr(j + 97)
                    freq[j] -= 1
                    break

            if not gtChar: continue

            ans = target[:i] + gtChar + "".join([chr(97 + j) * freq[j] for j in range(26)])
            return ans

        return ''

