class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = Counter(chars)
        ans = 0

        for word in words:
            chars_copy = chars_cnt.copy()

            for ch in word:
                if ch not in chars_copy or chars_copy[ch]==0:
                    break
                chars_copy[ch] -= 1

            else:
                ans += len(word)

        return ans
        