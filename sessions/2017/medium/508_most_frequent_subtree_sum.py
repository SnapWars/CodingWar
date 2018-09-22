class Solution(object):
    def findFrequentTreeSum(self, root):
        result = []
        if not root:
            return result

        def getSum(node, d):
            if not node:
                return 0
            _sum = node.val + getSum(node.left, d) + getSum(node.right, d)
            d[_sum] = 1 if _sum not in d else d[_sum] + 1
            return _sum

        d = {}
        getSum(root, d)
        most_freq = 0

        for key in d:
            if d[key] > most_freq:
                most_freq = d[key]
                result = [key]
            elif d[key] == most_freq:
                result.append(key)
        return result
