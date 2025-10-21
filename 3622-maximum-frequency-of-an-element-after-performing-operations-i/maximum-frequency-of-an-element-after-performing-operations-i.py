class Solution:
    def maxFrequency(self, nums: List[int], k: int, no: int) -> int:
        cnt = Counter(nums)
        end = max(nums)
        pref = [cnt[0]]

        for i in range(1, end + 1):
            pref.append(pref[-1] + cnt[i])

        ans = 0
        for i in range(end + 1):
            left = max(0, i - k)
            right = min(end, i + k)
            prefLeft = pref[left - 1] if left > 0 else 0
            prefRight = pref[right] if right < len(pref) else 0

            ans = max(ans, cnt[i] + min(no, prefRight - prefLeft - cnt[i]))

        return ans


        