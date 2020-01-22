# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            nr = TreeNode(d)
            nr.left = root
            return nr

        q = [(root, 1)]
        cur_l = 1
        parents = [root, root]
        while len(q) > 0:
            node, l = q.pop()
            if l == d:
                left = TreeNode(v)
                left.left = parents[0].left
                right = TreeNode(v)
                right.right = parents[1].right
                parents[0].left = left
                parents[1].right = right
                break
            elif l == d - 1:
                parents[0] = node
                parents[1] = q[-1][0] if len(q) > 0 else node

            if node.left:
                q.append((node.left, l + 1))
            if node.right:
                q.append((node.right, l + 1))
            if not node.left and not node.right and l == d - 1:
                left = TreeNode(v)
                left.left = parents[0].left
                right = TreeNode(v)
                right.right = parents[1].right
                parents[0].left = left
                parents[1].right = right
                break
        return root

                
