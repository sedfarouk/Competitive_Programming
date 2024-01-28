class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccur = defaultdict(int)
        monoStack = deque()
        present = set()

        for i in range(len(s)):
            lastOccur[s[i]] = i

        for i in range(len(s)):
            if s[i] not in present:
                while monoStack and monoStack[-1] > s[i] and lastOccur[monoStack[-1]] > i:
                    letter = monoStack.pop()
                    present.remove(letter)

                monoStack.append(s[i])
                present.add(s[i])

        return "".join(monoStack)
