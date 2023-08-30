class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        suffix = [0]*len(s)
        suffix[-1] = shifts[-1]

        for i in range(len(s)-2, -1, -1):
            suffix[i] = suffix[i+1] + shifts[i]

        ans = ""
        cnt = 0
        for i in range(len(s)):
            ans += chr((ord(s[i])-ord('a') + suffix[i]) % 26 + 97)
        return ans
 
        # cnt = 1
        # ans = s
        # for i in shifts:
        #     tmp = ""
        #     for j in range(cnt):
        #         tmp+=chr(ord(ans[j])+i)

        #     for j in range(cnt, len(ans)):
        #         tmp+=s[j]

        #     cnt+=1
        #     ans = tmp

        # return ans



        
