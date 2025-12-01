class Node:
    def __init__(self, val=-1):
        self.val = val


class RandomizedCollection:
    def __init__(self):
        self.keys = {}
        self.values = defaultdict(list)
        self.nodes = []


    def insert(self, val: int) -> bool:
        new_node = Node(val)

        self.keys[new_node] = len(self.nodes)
        self.nodes.append(new_node)
        self.values[val].append(new_node)

        return len(self.values[val]) == 1


    def remove(self, val: int) -> bool:
        if not self.values[val]:
            return False

        node = self.values[val].pop()
        self.nodes[self.keys[node]], self.nodes[-1] = self.nodes[-1], self.nodes[self.keys[node]]
        self.keys[self.nodes[self.keys[node]]] = self.keys[node]
        self.nodes.pop()
        del self.keys[node]

        return True

    def getRandom(self) -> int:
        return self.nodes[floor(random.random() * len(self.nodes))].val


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()