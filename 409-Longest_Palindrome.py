# 409. Leetcode - Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = Counter(s)
        evens, odds = [], []
        ans, odd_present = 0, 0

        for i in hashmap.values():
            if i%2==0:
                ans+=i
            else:
                ans+=i-1
                odd_present = 1
        return ans + odd_present
