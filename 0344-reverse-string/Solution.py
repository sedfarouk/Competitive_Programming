class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
#         left, right = 0, len(s)-1
        
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             right-=1
#             left+=1
        def reverse(self, left, right):
            if left >= right:
                return
            reverse(self, left+1, right - 1)
            s[left], s[right] = s[right], s[left]
        reverse(self, 0, len(s)-1)
            
            
