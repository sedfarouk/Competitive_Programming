class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        arr = []

        for r in bank:
            ones = r.count('1')
            if ones > 0:
                arr.append(ones)

        for i in range(1, len(arr)):
            ans += arr[i]*arr[i-1]

        return ans
        