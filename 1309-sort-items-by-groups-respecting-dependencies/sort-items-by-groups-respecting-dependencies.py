class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        itemsGraph, groupsGraph = defaultdict(lambda :defaultdict(list)), defaultdict(set)
        inGroups, inItems = [0] * m, [0] * n

        for i in range(n):
            if group[i] == -1:
                itemsGraph[m][i] = []
                group[i] = m
                inGroups.append(0)
                m += 1
            else:
                itemsGraph[group[i]][i] = []

        for i in range(n):
            for par in beforeItems[i]:
                if group[par] != group[i] and group[i] not in groupsGraph[group[par]]:
                    groupsGraph[group[par]].add(group[i])
                    inGroups[group[i]] += 1
                itemsGraph[group[par]][par].append(i)

            inItems[i] = len(beforeItems[i])

        queueGroup = deque([i for i in range(m) if inGroups[i] == 0])
        groupings = []
        while queueGroup:
            l = len(queueGroup)

            for _ in range(l):
                grp = queueGroup.popleft()

                for nei in groupsGraph[grp]:
                    inGroups[nei] -= 1

                    if inGroups[nei] == 0:
                        queueGroup.append(nei)

                groupings.append(grp)
        
        if queueGroup:
            return []

        ans = []
        for grp in groupings:
            queueItems = deque([i for i in itemsGraph[grp] if inItems[i] == 0])
            curr = []
            while queueItems:
                l = len(queueItems)

                for _ in range(l):
                    item = queueItems.popleft()

                    for nei in itemsGraph[grp][item]:
                        inItems[nei] -= 1

                        if inItems[nei] == 0 and group[nei] == grp:
                            queueItems.append(nei)
                    curr.append(item)

            if queueItems:
                return []
            ans.extend(curr)
        return ans if len(ans) == n else []

