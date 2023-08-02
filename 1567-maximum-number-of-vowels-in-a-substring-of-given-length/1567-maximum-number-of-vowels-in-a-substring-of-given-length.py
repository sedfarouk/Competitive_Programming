class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 1
        vowels = ['a','e','i','o','u']
        ans = float("-inf")
        temp = 0
        window = s[:k]

        for i in window:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                temp+=1
        ans = max(ans, temp)

        for right in range(k, len(s)):
            window = s[left:right]
            if s[right]=='a' or s[right]=='e' or s[right] =='i' or s[right]=='o' or s[right]=='u':
                temp+=1
            if s[left-1]=='a' or s[left-1]=='e' or s[left-1] =='i' or s[left-1]=='o' or s[left-1]=='u':
                temp-=1
            left+=1
            ans = max(ans, temp)
        return ans
            
