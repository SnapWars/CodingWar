# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = [[root.val]]
        visited = set([root])
        q = [(root, 0)]
        
        while q:
            node, level = q.pop(0)
            
            if len(result) < level+1:
                result.append([])
            
            if node not in visited:
                visited.add(node)
                result[level].append(node.val)
            
            if node.left and node.left not in visited:
                q.append((node.left, level + 1))
            if node.right and node.right not in visited:
                q.append((node.right, level + 1))
                
        return result
