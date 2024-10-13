class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        K = len(nums)
        arr = []

        for i, lst in enumerate(nums):
            for num in lst:
                arr.append([num, i])

        arr.sort()
        hashmap = defaultdict(int)

        res = []
        left = 0
        for right, num in enumerate(arr):
            hashmap[num[1]] += 1

            while len(hashmap)==K:
                if not res or arr[right][0] - arr[left][0] < res[1] - res[0]:
                    res = [arr[left][0], arr[right][0]]
                hashmap[arr[left][1]] -= 1
                if hashmap[arr[left][1]]==0:
                    hashmap.pop(arr[left][1])
                left += 1
        return res

            