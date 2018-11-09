class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set([0])
        q = [rooms[0]]

        while len(q) > 0:
            l = q.pop(0)
            for r in l:
                if r not in visited:
                    visited.add(r)
                    q.append(rooms[r])

        if len(visited) != len(rooms):
            return False
        return True
