class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        currKeys = set([i for i in range(n) if status[i]])
        currBoxes = set(initialBoxes)
        ans = 0

        visitedBoxes = set()
        while True:
            oper = False
            for box in list(currBoxes):
                if box in currKeys:
                    oper = True
                    ans += candies[box]
                    currKeys |= set(keys[box])
                    currBoxes |= set(containedBoxes[box]) - visitedBoxes
                    currBoxes.remove(box)
                    visitedBoxes.add(box)

            if not oper: return ans
