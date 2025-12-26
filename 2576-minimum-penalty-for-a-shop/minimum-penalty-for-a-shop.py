class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = penalty = n = len(customers)
        Y = customers.count('Y')
        N = 0

        for i in range(n + 1):
            if N + Y < penalty:
                ans = i 
                penalty = N + Y
        
            if i == n:
                continue

            Y -= int(customers[i] == 'Y')
            N += int(customers[i] == 'N')

        return ans