class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        reach = defaultdict(int)
        n, m = len(edges1), len(edges2)

        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)

        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        parity_checker = defaultdict(bool)
        e = o = 0
        def bfs(node, tree, f):
            nonlocal e, o
            queue = deque([(node, -1, 1)])
            vis = set([node])
            while queue:
                curr, par, cnt = queue.popleft()

                if cnt % 2:
                    parity_checker[curr] = False
                    o += 1
                else:
                    parity_checker[curr] = True
                    e += 1

                for nei in tree[curr]:
                    if nei not in vis:
                        queue.append((nei, curr, cnt + 1))
                        vis.add(nei)

        bfs(0, tree2, True)
        e1, o1 = e, o
        e = o = 0
        bfs(0, tree1, False)

        ans = []
        for i in range(n + 1):
            if parity_checker[i]:
                ans.append(e + max(e1, o1))
            else:
                ans.append(o + max(e1, o1))

        return ans
            
            

            