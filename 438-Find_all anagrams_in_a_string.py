# 438. Leetcode - Find all anagrams in a string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # p_count = Counter(p)
        # ans = []
        # k = len(p)
        # win = s[:k]

        # for right in range(k,len(s)+1):
        #     win = s[right-k:right]
        #     if Counter(win) == p_count:
        #         ans.append(right-k)

        if len(p) > len(s):
            return []

        arr_s = [0]*26
        arr_p = [0]*26
        m = len(p)
        ans = []

        for i in p:
            arr_p[ord(i)-ord('a')] += 1   

        for i in range(m):
            arr_s[ord(s[i])-ord('a')] += 1

        left, right = 0, m

        while right < len(s):
            if arr_s==arr_p:
                ans.append(left)
            arr_s[ord(s[right])-ord('a')]+=1
            arr_s[ord(s[left])-ord('a')]-=1
            left+=1
            right+=1
        
        if arr_s==arr_p:
            ans.append(left)
            
        return ans

            
