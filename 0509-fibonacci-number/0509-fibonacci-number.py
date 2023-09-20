class Solution:
    def __init__(self):
        self.hashmap = defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[self.fib(n)]
        if n <= 1:
            return n
        one = self.fib(n-1)
        two = self.fib(n-2)
        
        return one + two
        self.hashmap[n-1] = one
        self.hashmap[n-2] = two
        
        
        
        