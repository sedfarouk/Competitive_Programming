class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_valid_state(state):
            return len(set(state)) == len(state)
        
        def search(state, idx):
            maxx[-1] = max(maxx[-1], len(state))

            for i in range(idx, len(arr)):
                if is_valid_state(state + arr[i]):
                    search(state + arr[i], i+1)

        maxx =[float("-inf")]
        search("", 0)
        return maxx[-1]
                
                
        
