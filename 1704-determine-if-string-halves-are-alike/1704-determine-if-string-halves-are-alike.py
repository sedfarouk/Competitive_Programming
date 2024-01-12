class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u'}
        s = s.lower()
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        first, second = 0, 0

        for ch in s1:
            if ch in vowels:
                first += 1

        for ch in s2:
            if ch in vowels:
                second += 1
        print(s1, s2)
        return first==second

        
        