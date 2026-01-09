class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.currIdx = self.lastIdx = 0

    def visit(self, url: str) -> None:
        self.currIdx += 1

        if len(self.visited) <= self.currIdx:
            self.visited.append(url)
        else:
            self.visited[self.currIdx] = url
        self.lastIdx = self.currIdx

    def back(self, steps: int) -> str:
        self.currIdx = max(0, self.currIdx - steps)
        return self.visited[self.currIdx]

    def forward(self, steps: int) -> str:
        self.currIdx = min(self.lastIdx, self.currIdx + steps)
        return self.visited[self.currIdx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)