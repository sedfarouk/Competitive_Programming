class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            return len(state)==len(nums)

        def get_candidates(state):
            return set(nums)-set(state)

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        solutions = []
        search([], solutions)
        return solutions