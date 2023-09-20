class Solution:
    def __init__(self):
        self.hashmap = defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[n]
        if n <= 1:
            return n
        self.hashmap[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.hashmap[n]
        
        
        
        
        