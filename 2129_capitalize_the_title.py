# 2129. Leetcode - Capitalize the title

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        lst = title.split()

        for i in range(len(lst)):
            if len(lst[i])==1 or len(lst[i])==2:
                lst[i]=lst[i].lower()
            else:
                lst[i]=lst[i].title()

        return " ".join(lst)
