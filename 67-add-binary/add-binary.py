class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        ans = []
        carry = 0

        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2:
                ans.append('1')
            else:
                ans.append('0')
            
            carry //= 2

        if carry:
            ans.append('1')

        return "".join(ans[::-1])

        