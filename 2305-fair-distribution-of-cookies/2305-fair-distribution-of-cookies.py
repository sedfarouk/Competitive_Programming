class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = sum(cookies)
        childrenDistribution = [0] * k

        def distribute(childrenDistribution, idx):
            nonlocal ans
            if idx >= len(cookies):
                ans = min(ans, max(childrenDistribution))
                return

            for i in range(k):
                childrenDistribution[i] += cookies[idx]

                if childrenDistribution[i] < ans:
                    distribute(childrenDistribution, idx+1)
                childrenDistribution[i] -= cookies[idx]

        distribute(childrenDistribution, 0)
        return ans