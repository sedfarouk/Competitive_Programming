class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=''
        i = 0
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                val = int(s[i:i+2])
                ans+=chr(val+96)
                i+=3
            else:
                ans+=chr(int(s[i])+96)
                i+=1
        return ans