# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = [(root,1)]
        self.parent = {}
        depth = {}
        while len(q) > 0:
            node, l = q.pop()
            if l not in depth:
                depth[l] = [node]
            else:
                depth[l].append(node)
            if node.left:
                self.parent[node.left] = node
                q.append((node.left, l+1))
            if node.right:
                self.parent[node.right] = node
                q.append((node.right, l+1))
        _max = max(depth.keys())
        return self.lca(depth[_max])

    def lca(self, nodes):
        l = len(nodes)
        while len(set(nodes)) != 1:
            for i in xrange(l):
                nodes[i] = self.parent[nodes[i]]
        return nodes[0]
