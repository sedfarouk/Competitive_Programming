class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = Counter(secret)
        bulls = cows = 0

        for i in range(len(guess)):
            if guess[i] == secret[i] and hashmap[guess[i]] > 0:
                bulls += 1
                hashmap[guess[i]] -= 1

        for i in range(len(guess)):
            if guess[i] != secret[i] and hashmap.get(guess[i], 0) > 0:
                cows += 1
                hashmap[guess[i]] -= 1

        return f'{bulls}A{cows}B'
