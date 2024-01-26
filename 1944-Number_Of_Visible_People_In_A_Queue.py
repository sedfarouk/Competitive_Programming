class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        monostack = deque()
        seenPeople = [0] * n

        for i in range(n):
            while monostack and heights[monostack[-1]] <= heights[i]:
                person = monostack.pop()
                seenPeople[person] += 1

            if monostack:
                seenPeople[monostack[-1]] += 1
            monostack.append(i)

        return seenPeople
            
