class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        summ_r = [r.count(1) for r in grid]
        cols = list(map(list, zip(*grid)))
        summ_c = [c.count(1) for c in cols]
        return [[(2*r-len(grid))+(2*c-len(grid[0])) for c in summ_c] for r in summ_r]