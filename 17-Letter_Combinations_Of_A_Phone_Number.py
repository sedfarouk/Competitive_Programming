class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        solutions = []

        def backtrack(digit, idx):
            if len(digit)==len(digits) and digit:
                solutions.append(digit)
                
            for i in range(idx, len(digits)):
                for key in keypad[digits[i]]:
                    backtrack(digit+key, i+1)
                    
        backtrack("", 0)
        return solutions
                


        
