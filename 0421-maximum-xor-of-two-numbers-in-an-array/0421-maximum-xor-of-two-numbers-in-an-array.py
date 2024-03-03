class Trie:
    def __init__(self):
        self.root = {}

    def addNumber(self, num):
        curr = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in curr:
                curr[bit] = {}
            curr = curr[bit]

    def search(self, num):
        curr = self.root
        ans = 0

        for i in range(31, -1, -1):        
            bit = (num >> i) & 1
            if 1-bit in curr:
                ans |= 1<<i
                curr = curr[1-bit]
            else:
                curr = curr[bit]
        return ans

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for num in nums:
            trie.addNumber(num)

        maxx = float("-inf")
        for num in nums:
            maxx = max(maxx, trie.search(num))
        
        return maxx

        

        

