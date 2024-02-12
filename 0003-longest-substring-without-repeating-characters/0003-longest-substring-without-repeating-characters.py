class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # hashmap = Counter()
        # longest = 0
        
        # for right in range(len(s)):
        #     hashmap[s[right]]+=1
        #     while hashmap[s[right]]==2:
        #         hashmap[s[left]]-=1
        #         left+=1
        #     longest = max(longest, right-left+1)
        # return longest

        left = maxx_length = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]]+1
            seen[s[right]] = right
            maxx_length = max(maxx_length, right-left+1)
        return maxx_length
            

