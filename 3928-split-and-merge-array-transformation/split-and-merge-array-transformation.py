class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        queue = deque([(tuple(nums1), 0)])
        n = len(nums1)
        vis = set(tuple(nums1))

        while queue:
            q, d = queue.popleft()

            if q == tuple(nums2):
                return d

            for i in range(n):
                for j in range(n - 1, i - 1, -1):
                    sub = q[i:j+1]
                    new = q[:i] + q[j+1:]

                    for k in range(len(new)):
                        new_state = tuple(new[:k] + sub + new[k:])

                        if new_state not in vis:
                            queue.append((new_state, d+1))
                            vis.add(new_state)
