class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache
        def dp(i, num_a, num_l):
            if num_a >= 2:
                return 0
            if num_l >= 3:
                return 0
            if i == n:
                return 1
            
            
            P = dp(i + 1, num_a, 0)
            L = dp(i +1, num_a, num_l+1)
            A = dp(i+1, num_a+1, 0)

            return (P + L + A) % (10 ** 9 + 7)

        return dp(0, 0, 0)
        
        # MOD = 10**9 + 7
        # memo = {}
    
        # @lru_cache(100)
        # def dp(days: int, absent: bool, lateness: int) -> int:
        #     # Base case
        #     if days == 0:
        #         return 1
            
        #     # check if states are memoized
        #     if (days, absent, lateness) in memo:
        #         return memo[(days, absent, lateness)]
            
        #     if absent:
        #         option1 = dp(days-1, True, 0) # present on that day
        #         if lateness < 2:    
        #             return (option1 + dp(days-1, True, lateness + 1)) % MOD 
        #         return option1
            
        #     else:
        #         option1 = dp(days-1, True, 0) # absent on that day
        #         option2 = dp(days-1, False, 0) # present on that day
                
        #         if lateness < 2:
        #             option3 = dp(days-1, False, lateness + 1) # late on that day
        #             return (option1 + option2 + option3) % MOD
                
        #         return (option1 + option2) % MOD
        
        # return dp(n, False, 0) % MOD