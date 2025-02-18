class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        arr = [0] * length
        used = [False] * n

        def backtrack(curr):
            while curr < length and arr[curr] != 0:
                curr += 1
                
            if curr == length:
                return True 

            for x in range(n, 0, -1):
                if x == 1 and not used[x - 1] and arr[curr] == 0:
                    arr[curr] = x
                    used[x - 1] = True

                    if backtrack(curr + 1):
                        return True
                    arr[curr] = 0
                    used[x - 1] = False

                elif not used[x - 1] and curr + x < length and arr[curr] == 0 and arr[curr + x] == 0:
                    arr[curr] = arr[curr + x] = x
                    used[x - 1] = True

                    if backtrack(curr + 1):
                        return True
                    arr[curr] = arr[curr + x] = 0
                    used[x - 1] = False
                    
            return False

        backtrack(0)
        return arr

                 
                     