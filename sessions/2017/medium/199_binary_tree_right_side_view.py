class Solution(object):
    def rightSideView(self, root):
        queue = [(root, 0)]
        last_level = None
        last_node = None
        result = []

        while len(queue) > 0:
            node, level = queue.pop(0)

            if node is None:
                continue
            if last_level != level:
                result.append(node.val)
            last_level = level
            last_node = node

            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))

        return result
