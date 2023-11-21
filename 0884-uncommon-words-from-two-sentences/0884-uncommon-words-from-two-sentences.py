class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        hashmap = Counter(s1 + s2)
        
        return [key for key, val in hashmap.items() if val==1]
    
