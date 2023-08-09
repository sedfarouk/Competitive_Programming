# 409. Leetcode - Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = Counter(s)
        evens, odds = [], []

        for i in hashmap.values():
            if i%2==0:
                evens.append(i)
            else:
                odds.append(i)

        odds.sort(reverse=True)
        sum_evens = sum(evens)

        odds_sum = 0
        for i in odds:
            if i>1:
                odds_sum+=i-1

        if odds!=[]:
            return sum_evens + odds_sum + 1
        return sum_evens
            
