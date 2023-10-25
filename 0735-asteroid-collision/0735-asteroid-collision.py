class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for asteroid in asteroids:
            if not stack or (stack[-1] < 0 and asteroid > 0) or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0):
                stack.append(asteroid)

            else:
                neg_val = abs(asteroid)

                if stack[-1] > neg_val:
                    continue

                while stack and neg_val >= stack[-1] and stack[-1] > 0 and asteroid != 0:
                    removed = stack.pop()

                    if removed == neg_val:
                        asteroid = 0

                if (asteroid < 0 and stack and stack[-1] < neg_val) or (not stack and asteroid < 0):
                    stack.append(asteroid)

        return stack