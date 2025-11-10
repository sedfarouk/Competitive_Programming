class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        currKeys = set([i for i in range(n) if status[i]])
        queue = deque()
        visitedBoxes, boxesToSearch = set(), set()
        ans = 0

        for initialBox in initialBoxes:
            if status[initialBox]:
                queue.append(initialBox)
                visitedBoxes.add(initialBox)
            else:
                boxesToSearch.add(initialBox)

        while queue:
            q = queue.popleft()
            ans += candies[q]

            for key in keys[q]:
                if key not in visitedBoxes:
                    if key in boxesToSearch:
                        queue.append(key)
                        boxesToSearch.remove(key)
                        visitedBoxes.add(key)
                    else:
                        currKeys.add(key)

            for box in containedBoxes[q]:
                if box not in visitedBoxes:
                    if box in currKeys:
                        queue.append(box)
                        visitedBoxes.add(box)
                        
                    else:
                        boxesToSearch.add(box)

        return ans






            