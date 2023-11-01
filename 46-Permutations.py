class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:             
        def is_valid_state(state):
            if len(state)==len(nums):
                return True

        def get_candidates(state):
            if not state:
                return nums

            return [num for num in nums if num not in state]

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.remove(candidate)

        
        solutions = []
        state = list()
        search(state, solutions)
        return solutions
