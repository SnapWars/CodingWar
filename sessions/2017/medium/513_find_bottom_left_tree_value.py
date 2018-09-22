class Solution(object):
    def findBottomLeftValue(self, root):
        queue = [root]
        last = None
        while len(queue) > 0:
            node = queue.pop(0)
            last = node
            if node is None:
                continue
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return last.val
