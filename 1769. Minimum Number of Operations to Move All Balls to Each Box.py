class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pref = [0] 
        count = [0]

        for i in range(n):
            pref.append(pref[-1] + (i + 1 if boxes[i] == '1' else 0))
            count.append(count[-1] + int(boxes[i]))

        ans = []
        for i in range(1, n + 1):
            left = (i * count[i - 1]) - pref[i - 1]
            right = (pref[-1] - pref[i]) - i * (count[-1] - count[i])

            ans.append(left + right)
        return ans
