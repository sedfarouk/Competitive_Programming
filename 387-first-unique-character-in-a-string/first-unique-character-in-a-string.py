class Solution:
    def firstUniqChar(self, s: str) -> int:
        st = set()
        seen = set()
        n = len(s)

        for i in range(n):
            present = s[i] in seen 

            if present and s[i] in st:
                st.remove(s[i])
            elif not present:
                st.add(s[i])
                seen.add(s[i])

        for i in range(n):
            if s[i] in st:
                return i
        return -1

            