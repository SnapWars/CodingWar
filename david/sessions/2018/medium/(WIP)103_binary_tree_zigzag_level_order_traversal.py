# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return

        self.result = []
        self.helper(root)
        return self.result

    def helper(self, root):
        q = [(root, 0)]
        cur_level = 0
        temp = []
        while len(q) > 0:
            node, l = q.pop()
            print node.val
            if l != cur_level:
                self.result.append(temp)
                temp = []
                cur_level = l
            else:
                temp.insert(0, node.val)
            if l % 2 == 0:
                if node.right:
                    q.append((node.right, l+1))
                if node.left:
                    q.append((node.left, l+1))
            else:
                if node.left:
                    q.append((node.left, l+1))
                if node.right:
                    q.append((node.right, l+1))
                
