# 1456. Leetcode - maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 1
        vowels = ['a','e','i','o','u']
        ans = float("-inf")
        temp = 0

        for i in range(k):
            if s[i] in vowels:
                temp+=1
        ans = temp

        for right in range(k, len(s)):
            if s[right] in vowels:
                temp+=1
            if s[left-1] in vowels:
                temp-=1
            left+=1
            ans = max(ans, temp)
        return ans
            
