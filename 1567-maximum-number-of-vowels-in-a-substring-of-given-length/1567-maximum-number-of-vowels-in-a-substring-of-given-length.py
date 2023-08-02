class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 1
        vowels = ['a','e','i','o','u']
        ans = float("-inf")
        temp = 0
        window = s[:k]

        for i in window:
            if i in vowels:
                temp+=1
        ans = max(ans, temp)

        for right in range(k, len(s)):
            window = s[left:right]
            if s[right] in vowels:
                temp+=1
            if s[left-1] in vowels:
                temp-=1
            left+=1
            ans = max(ans, temp)
        return ans
            
