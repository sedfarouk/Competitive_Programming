class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0]

        for h in height:
            pref.append(pref[-1])

            if h > pref[-1]:
                pref[-1] = h

        ans = max_h = 0
        for i in range(len(height) - 1, -1, -1):
            ans += max(0, min(max_h, pref[i]) - height[i])
            max_h = max(max_h, height[i])

        return ans
