class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for i in strs:
            ana = ''.join(sorted(list(i)))
            if ana not in sets:
                sets[ana] = [i]
            else:
                sets[ana].append(i)
        return list(sets.values())