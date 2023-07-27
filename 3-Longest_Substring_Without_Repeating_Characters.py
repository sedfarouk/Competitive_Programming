# 3. Leetcode - Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hashmap = Counter()
        longest = 0
        
        for right in range(len(s)):
            hashmap[s[right]]+=1
            while hashmap[s[right]]==2:
                hashmap[s[left]]-=1
                left+=1
            longest = max(longest, right-left+1)
        return longest
