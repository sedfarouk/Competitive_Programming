class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        comb = []

        def backtrack(i):
            if i == len(digits):
                solutions.append("".join(comb))
                return

            for ch in letters[digits[i]]:
                comb.append(ch)
                backtrack(i + 1)
                comb.pop()

        solutions = []
        backtrack(0)
        return solutions
