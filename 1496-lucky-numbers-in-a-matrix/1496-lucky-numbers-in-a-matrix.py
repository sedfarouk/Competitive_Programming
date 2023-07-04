class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        cols = list(map(list, zip(*matrix)))
        for i in range(len(matrix)):
            r_set = min(set(matrix[i]))

            for j in range(len(matrix[0])):
                c_set = max(set(cols[j]))
                if r_set == c_set:
                    ans.append(r_set)
        return ans