class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(x) for x in range(1, n+1)]
        k -= 1
        ans = ""

        while len(digits) > 0:
            fact = math.factorial(len(digits)-1)
            idx = k // fact
            ans += digits[idx]
            digits.pop(idx)
            k %= fact

        return ans

        # solutions = []

        # def backtrack(s):
        #     if len(solutions)==k:
        #         return

        #     if len(s)==n:
        #         solutions.append(s)
        #         return 

        #     for i in range(1, n+1):
        #         if i not in s:
        #             backtrack(s+[i])
                    
        # backtrack([])
        # return "".join(map(str, solutions[-1]))