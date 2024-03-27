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
        for idx, val in enumerate(diff_arr[1:n+1]):
            new_val = ord(s[idx]) + val

            if new_val < 97:
                new_val = 122-((96-new_val)%26)
            elif new_val > 122:
                new_val = 97+((new_val-123) % 26)
            ans += chr(new_val)

        return ans

