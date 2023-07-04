class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_nums, max_nums, ans = [], [], []
        cols = list(map(list, zip(*matrix)))
        for i in range(len(matrix)):
            min_nums.append(min(set(matrix[i])))

        for j in range(len(matrix[0])):
            max_nums.append(max(set(cols[j])))
        
        for i in min_nums:
            if i in max_nums:
                ans.append(i)
        return ans