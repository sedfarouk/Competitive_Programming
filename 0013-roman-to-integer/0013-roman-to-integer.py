class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        ans = 0

        ptr = 0
        while ptr < len(s):
            if s[ptr:ptr+2]=='IV':
                ans += 4
                ptr += 2
            elif s[ptr:ptr+2]=='IX':
                ans += 9
                ptr += 2
            elif s[ptr:ptr+2]=='XL':
                ans += 40
                ptr += 2
            elif s[ptr:ptr+2]=='XC':
                ans += 90
                ptr += 2
            elif s[ptr:ptr+2]=='CD':
                ans += 400
                ptr += 2
            elif s[ptr:ptr+2]=='CM':
                ans += 900
                ptr += 2
            else:
                ans += hashmap[s[ptr]]
                ptr += 1

        return ans

        