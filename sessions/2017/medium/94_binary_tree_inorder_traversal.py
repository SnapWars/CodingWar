class Solution(object):
    '''def inorderTraversal(self, root):
        result = []
        def traverse(root, result):
            if not root:
                return result
            traverse(root.left, result)
            result.append(root.val)
            traverse(root.right, result)
            return result

        return traverse(root, result)'''

    def inorderTraversal(self, root):
        stack = []
        result = []
        current = root
        done = False
        while not done:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    result.append(current.val)
                    current = current.right
                else:
                    done = True
        return result
