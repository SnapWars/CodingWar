class Solution(object):
    def largestValues(self, root):
        queue = [(root, 0)]
        maxes = []

        while len(queue) > 0:
            (node, level) = queue.pop(0)
            if not node:
                continue
            if level == len(maxes):
                maxes.append(node.val)
            elif node.val > maxes[level]:
                maxes[level] = node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return maxes
