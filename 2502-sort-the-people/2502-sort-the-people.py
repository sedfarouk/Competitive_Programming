class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = []
        for i in range(len(names)):
            data.append([names[i],heights[i]])
        data.sort(key = lambda x:x[1], reverse=True)
        return [i[0] for i in data]