class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = [1 for i in range(right+1)]
        arr[0] = arr[1] = 0
        primes = []
        
        for i in range(2, int(sqrt(right+1))+1):
            if arr[i]==1:
                for j in range(i*i, right+1, i):
                    arr[j] = 0

        for i in range(left, len(arr)):
            if arr[i]==1: primes.append(i)
    
        if len(primes) < 2:
            return [-1, -1]
            
        ans = []
        diff = float("inf")
        for i in range(1, len(primes)):
            if (primes[i]-primes[i-1]) < diff:
                ans = [primes[i-1], primes[i]]
                diff = primes[i]-primes[i-1]
                
        return ans
                
        
        
