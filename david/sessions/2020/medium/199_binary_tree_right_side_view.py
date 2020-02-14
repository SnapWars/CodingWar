# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [(root, 0)]
        visited = {root}
        result = {}
        
        while queue:
            node, level = queue.pop(0)
            
            if level not in result:
                result[level] = [node.val]
            else:
                result[level].append(node.val)
            
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append((node.left, level + 1))
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append((node.right, level + 1))

        return [result[i][-1] for i in result]
