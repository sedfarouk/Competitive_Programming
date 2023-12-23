class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = set([(0, 0)])

        ini = (0, 0)
        for dir in path:
            if dir=="N":
                ini = (ini[0]-1, ini[1])

            elif dir=="S":
                ini = (ini[0]+1, ini[1])

            elif dir=="E":
                ini = (ini[0], ini[1]+1)

            else:
                ini = (ini[0], ini[1]-1)

            if ini in coords:
                return True
            coords.add(ini)
            
        return False