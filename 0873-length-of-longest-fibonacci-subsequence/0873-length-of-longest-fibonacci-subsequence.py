class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        hashmap = {arr[i]:i for i in range(n)}
        dp = [[2 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(i):
                diff = arr[i]-arr[j]
                if diff in hashmap and hashmap[diff] < j:
                    k = hashmap[diff] 
                    dp[j][i] = max(dp[j][i], dp[k][j] + 1)

        ans = max([max(n) for n in dp])
        return 0 if ans==2 else ans