MAXX = 10**6 + 1
isPrime = [True] * MAXX

class Solution:
    def fill(self):
        isPrime[0] = isPrime[1] = False
        for i in range(2, MAXX):
            if isPrime[i]:
                for j in range(i + i, MAXX, i):
                    isPrime[j] = False

    def minJumps(self, nums: List[int]) -> int:
        if isPrime[0]: self.fill()
        
        n = len(nums)
        hmap = defaultdict(list)   
        mx = max(nums)

        for i in range(n): hmap[nums[i]].append(i)         

        vis = set([0])
        queue = deque([(0, 0)])
        while queue:
            idx, steps = queue.popleft()

            if idx == n - 1:
                return steps

            if idx + 1 < n and (idx + 1) not in vis:
                queue.append((idx + 1, steps + 1))
                vis.add(idx + 1)

            if idx - 1 > 0 and (idx - 1) not in vis:
                queue.append((idx - 1, steps + 1))
                vis.add(idx - 1)

            if not isPrime[nums[idx]]: continue

            for i in range(nums[idx], mx + 1, nums[idx]):
                for j in hmap[i]:
                    if j not in vis: 
                        queue.append((j, steps + 1))
                        vis.add(j)
                del hmap[i]



            

            