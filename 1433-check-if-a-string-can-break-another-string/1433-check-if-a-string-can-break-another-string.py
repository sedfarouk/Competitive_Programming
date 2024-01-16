class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_lst, s2_lst = [], []

        for i in range(len(s1)):
            s1_lst.append(s1[i]) 
            s2_lst.append(s2[i]) 

        s1_lst.sort()
        s2_lst.sort()

        s1_break, s2_break = True, True
        for i in range(len(s1)):
            if s1_lst[i] < s2_lst[i]:
                s1_break = False
            if s2_lst[i] < s1_lst[i]:
                s2_break = False
        return s1_break or s2_break
