class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False

        s += s
        n, m = len(s), len(goal)
        goalLps = [0] * m

        i, j = 0, 1
        while j < m:
            if goal[i] == goal[j]:
                goalLps[j] = i + 1
                i += 1; j += 1

            elif i == 0:
                j += 1

            else:
                i = goalLps[i - 1]

        i = j = 0
        while j < n:
            if s[j] == goal[i]:
                i += 1; j += 1
            
            elif i == 0:
                j += 1

            else:
                i = goalLps[i - 1]

            if i == m:
                return True

        return False