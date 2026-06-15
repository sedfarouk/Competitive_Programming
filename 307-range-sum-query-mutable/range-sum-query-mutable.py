class NumArray:
    def __init__(self, nums: List[int]):
        self.sz = 1

        while self.sz < len(nums): self.sz *= 2

        self.sums = [0] * (self.sz * 2)
        self.build(nums, 0, 0, self.sz)

    def build(self, arr, node, lx, rx):
        if rx - lx == 1:
            if lx < len(arr):
                self.sums[node] = arr[lx]
            return

        m = (lx + rx) // 2

        self.build(arr, 2 * node + 1, lx, m)
        self.build(arr, 2 * node + 2, m, rx)

        self.sums[node] = self.sums[2 * node + 1] + self.sums[2 * node + 2]

    def setValue(self, idx, val, node, lx, rx):
        if rx - lx == 1:
            self.sums[node] = val
            return

        m = (lx + rx) // 2

        if idx < m: self.setValue(idx, val, 2 * node + 1, lx, m)
        else: self.setValue(idx, val, 2 * node + 2, m, rx)

        self.sums[node] = self.sums[2 * node + 1] + self.sums[2 * node + 2]

    def update(self, index: int, val: int) -> None:
        self.setValue(index, val, 0, 0, self.sz)

    def queryRange(self, l, r, node, lx, rx):
        if l >= rx or r <= lx: return 0
        if l <= lx and r >= rx: return self.sums[node]

        m = (lx + rx) // 2

        s1 = self.queryRange(l, r, 2 * node + 1, lx, m)
        s2 = self.queryRange(l, r, 2 * node + 2, m, rx)

        return s1 + s2

    def sumRange(self, left: int, right: int) -> int:
        return self.queryRange(left, right + 1, 0, 0, self.sz)       


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)