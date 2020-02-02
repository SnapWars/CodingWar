class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination:
            return True
        
        self.directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]

        q = [start]
        visited = set(self.to_tuple(start))
        
        while q:
            popped = q.pop(0)
            
            if popped[0] == destination[0] and popped[1] == destination[1]:
                visited.add(self.to_tuple(destination))
                break
            
            for terminal_point in self.get_next_terminal_points(popped, maze):
                if terminal_point not in visited:
                    visited.add(terminal_point)
                    q.append(terminal_point)
    
        return self.to_tuple(destination) in visited

    
    def add_as_tuple(self, c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1])
    
    def subtract_as_tuple(self, c1, c2):
        return (c1[0] - c2[0], c1[1] - c2[1])

    def to_tuple(self, lst):
        return (lst[0], lst[1])
    
    def bound_check(self, pos, maze):
        return pos[0] >= 0 and pos[0] < len(maze) and pos[1] >= 0 and pos[1] < len(maze[0])

    def get_next_terminal_points(self, pos, maze):
        result = []

        for direction in self.directions:
                next_with_offset = self.add_as_tuple(pos, direction)
                
                # God damn, gotta keep rolling >:(
                while self.bound_check(next_with_offset, maze) and maze[next_with_offset[0]][next_with_offset[1]] == 0:
                    next_with_offset = self.add_as_tuple(next_with_offset, direction)
                
                # Unwind to last valid position
                prev_pos = self.subtract_as_tuple(next_with_offset, direction)
                if prev_pos != pos:
                    result.append(prev_pos)
        
        return result
