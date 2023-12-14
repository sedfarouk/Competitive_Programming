class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            new_key = queue.pop()
            room = rooms[new_key]
            visited.add(new_key)

            for key in room:
                if key not in visited:
                    queue.append(key)

        return len(visited) == len(rooms)
                    
