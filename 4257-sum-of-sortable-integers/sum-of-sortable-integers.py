MAXX = 10 ** 5

DIVS = [[] for _ in range(MAXX + 1)]
for i in range(1, MAXX + 1):
    for j in range(i, MAXX + 1, i):
        DIVS[j].append(i)


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        arr = nums

        for k in DIVS[n]:
            sortable = True
            prevMx = -10**18
            prevMn = -10**18

            for i in range(0, n, k):
                br = 0
                currMx = currMn = arr[i]

                for j in range(1, k):
                    cur = arr[i + j]
                    prev = arr[i + j - 1]

                    if cur < prev:
                        br += 1
                        if br > 1:
                            break

                    if cur > currMx:
                        currMx = cur
                    if cur < currMn:
                        currMn = cur

                if br == 1 and arr[i] < arr[i + k - 1]:
                    br += 1

                if br > 1 or prevMx > currMx or prevMn > currMn or prevMx > currMn:
                    sortable = False
                    break

                prevMx = currMx
                prevMn = currMn

            if sortable:
                ans += k

        return ans