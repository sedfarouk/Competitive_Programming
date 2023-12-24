class Solution:
    def minOperations(self, s: str) -> int:
        if len(s)==1: return 0
            
        one = '01' * (len(s)//2) + '0' * (len(s)%2)
        two = '10' * (len(s)//2) + '1' * (len(s)%2)
        
        first = second = 0
        for i in range(len(one)):
            if s[i]!=one[i]:
                first += 1
        
        for i in range(len(two)):
            if s[i]!=two[i]:
                second += 1
                
        return min(first, second)

        