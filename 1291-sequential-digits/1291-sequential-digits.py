class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        queue = deque(range(1, 10))

        # Essentially, we are just enumerating all possible values (combinations), hence bfs is a good candidate to solve this problem
        # Think of the space tree
 
        while queue:
            digit = queue.popleft()

            if low <= digit <= high:
                ans.append(digit)

            last_digit = digit % 10
            if last_digit < 9:
                queue.append(digit*10+last_digit+1)

        return ans

        