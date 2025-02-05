class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap1, swap2 = [], []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if len(swap1) == 2:
                    return False
                
                swap1.append(s1[i])
                swap2.append(s2[i])
        
        if len(swap1) == 1:
            return False
        
        if len(swap1) == 2:
            return swap1[0] == swap2[1] and swap1[1] == swap2[0]
        
        return True