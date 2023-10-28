class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:   
        def is_valid_state(state):
            if len(state) == k:
                return True
            return False

        def get_candidates(state):
            start = max(state) if state else 1
            lst = []

            for i in range(start, n+1):
                if i not in state:
                    lst.append(i)
            return lst

        def search(state, solution):
            if is_valid_state(state):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        return solutions

            