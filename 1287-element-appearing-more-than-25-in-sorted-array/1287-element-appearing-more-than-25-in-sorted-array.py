class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arrCnt = Counter(arr)
        maxx_freq = max(list(arrCnt.values()))

        for key, val in arrCnt.items():
            if val==maxx_freq:
                return key