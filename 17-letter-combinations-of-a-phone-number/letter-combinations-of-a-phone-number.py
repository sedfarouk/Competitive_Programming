class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        n = len(digits)
        res, curr = [], []

        def backtrack(i):
            if i == n:
                res.append(curr.copy())
                return

            for c in letters[digits[i]]:
                curr.append(c)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return ["".join(soln) for soln in res]