MAXX = 1000000
primes = [True] * (MAXX + 2)
primes[0] = primes[1] = False
MULT = defaultdict(list)

for i in range(2, MAXX + 1):
    if primes[i]:
        MULT[i].append(i)
        for j in range(i * 2, MAXX + 1, i):
            primes[j] = False
            MULT[i].append(j)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        indexes = defaultdict(list)
        mx = max(nums)

        for idx, num in enumerate(nums):
            indexes[num].append(idx)

        queue = deque([0])
        vis = set([0])
        used_primes = set()

        ans = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == n - 1:
                    return ans

                if curr < n - 1 and (curr + 1) not in vis:
                    vis.add(curr + 1)
                    queue.append(curr + 1)

                if curr > 0 and (curr - 1) not in vis:
                    vis.add(curr - 1)
                    queue.append(curr - 1)

                if primes[nums[curr]] and nums[curr] not in used_primes:
                    used_primes.add(nums[curr])

                    for num in MULT[nums[curr]]:
                        if num > mx: break
                        for idx in indexes[num]:
                            if idx not in vis:
                                vis.add(idx)
                                queue.append(idx)

            ans += 1