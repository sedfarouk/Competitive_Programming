class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_arr = [0]*(n+2)

        for shift in shifts:
            l, r, dirr = shift[0], shift[1], shift[2]
            val = 1 if dirr else -1 
            diff_arr[l+1] += val
            diff_arr[r+2] -= val

        for i in range(1, n+2):
            diff_arr[i] += diff_arr[i-1]

        ans = ""
        for i in range(n):
            char = ord(s[i])-ord('a')
            char += diff_arr[i+1]
            char %= 26
            ans += chr(char+ord("a"))

        return ans

