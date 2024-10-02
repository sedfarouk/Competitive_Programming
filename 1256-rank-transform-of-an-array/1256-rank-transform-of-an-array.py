class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        order = {}
        i = 1

        for val in sorted(arr):
            if val not in order:
                order[val] = i
                i += 1
        return [order[val] for val in arr]