class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currTabIdx = 0

    def visit(self, url: str) -> None:
        self.clearForward()
        self.history.append(url)
        self.currTabIdx += 1

    def back(self, steps: int) -> str:
        while steps > 0 and self.currTabIdx > 0:
            self.currTabIdx -= 1
            steps -= 1

        return self.history[self.currTabIdx]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.currTabIdx < len(self.history) - 1:
            self.currTabIdx += 1
            steps -= 1

        return self.history[self.currTabIdx]
    
    def clearForward(self):
        while len(self.history) != self.currTabIdx + 1:
            self.history.pop()

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)