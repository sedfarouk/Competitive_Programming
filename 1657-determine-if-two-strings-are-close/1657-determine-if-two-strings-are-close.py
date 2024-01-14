class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_1, count_2 = Counter(word1), Counter(word2)
        vals_1, vals_2 = Counter(count_1.values()), Counter(count_2.values())
        
        if count_1==count_2:
            return True
        
        if count_1.keys()!=count_2.keys():
            return False
        
        for key, val in vals_1.items():
            vals_2[key] -= val
            
        for val in vals_2.values():
            if val!=0:
                return False
        
        return True
        