class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:             
        def is_valid_state(state):
            if len(state)==len(nums):
                return True

        def get_candidates(state):
            return set(nums) - set(state)

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        
        solutions = []
        state = []
        search(state, solutions)
        return solutions
