class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base = 31
        mod = 10 ** 9 + 7
        prefix_hash = [0] * (n + 1)
        suffix_hash = [0] * (n + 1)
        power = [1] * (n + 1)
        rev_s = s[::-1]

        def get_hash(l, r, hash_arr):
            return (hash_arr[r] - hash_arr[l] * power[r - l] % mod + mod) % mod

        for i in range(1, n + 1):
            power[i] = (power[i - 1] * base) % mod
            prefix_hash[i] = (prefix_hash[i - 1] * base + ord(s[i - 1])) % mod
            suffix_hash[i] = (suffix_hash[i - 1] * base + ord(rev_s[i - 1])) % mod 

        def is_palindrome(length):
            return get_hash(0, length, prefix_hash) == get_hash(n - length, n, suffix_hash)

        best = 0
        for i in range(1, n + 1):
            if is_palindrome(i):
                best = i 
        return s[best:][::-1] + s
