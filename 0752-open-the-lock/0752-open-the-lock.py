class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if "0000" in deadends: return -1

        def generate_seqs(pattern):
            combinations = []

            for i in range(len(pattern)):
                first = pattern[:i]+str((int(pattern[i])+1)%10) + pattern[i+1:]
                second = pattern[:i]+str((int(pattern[i])-1)%10) + pattern[i+1:]

                if int(pattern[i])-1==-1:
                    second = pattern[:i] + "9" + pattern[i+1:]

                if first not in deadends:
                    combinations.append(first)
                
                if second not in deadends:
                    combinations.append(second)

            return combinations

        queue = deque(["0000"])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                q = queue.popleft()

                if q == target:
                    return steps

                for combination in generate_seqs(q):
                    if combination not in deadends:
                        deadends.add(combination)
                        queue.append(combination)
            
            steps += 1  
        return -1
                
                