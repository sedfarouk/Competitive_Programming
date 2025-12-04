class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPal(ptr):
            used = False
            l, r = 0, len(s) - 1
            
            while l <= r:
                if s[l] == s[r]:
                    l += 1; r -= 1
                else:
                    if used:
                        return False
                    l += 1 if ptr == 'l' else 0
                    r -= 1 if ptr == 'r' else 0
                    used = True
            return True
        
        return checkPal("l") or checkPal("r")