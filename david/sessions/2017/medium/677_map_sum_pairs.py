class MapSum(object):

    def __init__(self):
        self.root = {}
        self.keys = {}

    def insert(self, key, val):
        traverse = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        for c in key:
            if c not in traverse:
                traverse[c] = {'value': val}
            else:
                traverse[c]['value'] += delta
            traverse = traverse[c]

    def sum(self, prefix):
        traverse = self.root
        for c in prefix:
            if c not in traverse:
                return 0
            traverse = traverse[c]
        return traverse['value']
