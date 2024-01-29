class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            return len(state)==len(nums)
        
        def get_candidates(count):
            possible = []

            for x in count:
                if count[x] > 0:
                    possible.append(x)

            return possible
        
        def search(state, solutions, count):
            if is_valid_state(state):
                solutions.append(state.copy())
                return
            
            for candidate in get_candidates(count):
                state.append(candidate)
                count[candidate] -= 1
                search(state, solutions, count)
                state.pop()
                count[candidate] += 1

        solutions = []
        state = []
        search(state, solutions, Counter(nums))
        return solutions