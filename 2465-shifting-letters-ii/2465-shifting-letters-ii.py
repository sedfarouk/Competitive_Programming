class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_arr = [0] * (n + 2)
        mp = [-1, 1]

        for shift in shifts:
            l, r, d = shift
            diff_arr[l + 1] += mp[d]
            diff_arr[r + 2] -= mp[d]

        for i in range(1, n + 1):
            diff_arr[i] += diff_arr[i - 1]

        ans = []
        for i in range(n):
            pos = ord(s[i]) - ord('a')
            new = (((pos + diff_arr[i + 1]) % 26) + 26) % 26
            ans.append(chr(new + ord('a')))
        
        return "".join(ans)
