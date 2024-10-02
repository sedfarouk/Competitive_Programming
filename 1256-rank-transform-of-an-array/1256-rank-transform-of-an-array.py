class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        order = {val: i+1 for i, val in enumerate(sorted(set(arr)))}
        return [order[val] for val in arr]