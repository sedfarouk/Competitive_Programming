class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def is_valid_state(state):
            return sum(state)==target
        
        def get_candidates(state):
            if sum(state) > target:
                return []
            
            if not state:
                return candidates
            
            possible = []
            for num in candidates:
                if num >= state[-1]:
                    possible.append(num)
            return possible
        
        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()
                
        solutions = []
        state = []
        search(state, solutions)
        return solutions