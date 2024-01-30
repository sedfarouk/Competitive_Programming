class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = sum(cookies)
        childrenDistribution = [0] * k

        def distribute(childrenDistribution, idx, maxx):
            nonlocal ans
            if idx >= len(cookies):
                ans = min(ans, maxx)
                return

            for i in range(k):
                childrenDistribution[i] += cookies[idx]

                if childrenDistribution[i] < ans:
                    distribute(childrenDistribution, idx+1, max(maxx, childrenDistribution[i]))
                childrenDistribution[i] -= cookies[idx]

        cookies.sort(reverse=True)
        distribute(childrenDistribution, 0, float("-inf"))
        return ans