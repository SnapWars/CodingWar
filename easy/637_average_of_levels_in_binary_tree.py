class Solution(object):
    def averageOfLevelsHelper(self, root, level, _map):
        if not root:
            return

        if level not in _map:
            _map[level] = []
        _map[level].append(root.val)
        self.averageOfLevelsHelper(root.left, level + 1, _map)
        self.averageOfLevelsHelper(root.right, level + 1, _map)

    def averageOfLevels(self, root):
        _map = {}
        self.averageOfLevelsHelper(root, 0, _map)

        result = []
        for key in sorted(_map.keys()):
            a = _map[key]
            result.append(float(sum(a))/len(a))
        return result
