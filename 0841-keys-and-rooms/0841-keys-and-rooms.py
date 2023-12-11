class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            boundary = len(queue)

            for _ in range(boundary):
                key = queue.pop()
                available = rooms[key]
                visited.add(key)

                for key in available:
                    if key not in visited:
                        queue.append(key)

        if len(visited) == len(rooms):
            return True
        return False
                    
