class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)

        def countLCT(x):
            l = lc = lct = 0

            for i in range(n + 1):
                if x[i] == 'L':
                    l += 1
                elif x[i] == 'C':
                    lc += l
                elif x[i] == 'T':
                    lct += lc
            return lct

        pref = [0]
        t = mx = d = c = 0

        for i in range(n):
            pref.append(pref[-1] + (s[i] == 'L'))
        
        for i in range(n-1, -1, -1):
            t += s[i] == 'T'
            if pref[i] + t >= mx:
                if pref[i] + t == mx and abs(pref[i] - t) > d:
                    continue
                c = i
                mx = pref[i] + t
                d = abs(pref[i] - t)

        return max(countLCT("L" + s), countLCT(s[:c] + "C" + s[c:]), countLCT(s + "T"))