class Trie(object):

    def __init__(self):
        self.root = {}


    def insert(self, word):
        traverse = self.root
        for c in word:
            if c not in traverse:
                traverse[c] = {}
            traverse = traverse[c]
        traverse['END'] = word

    def search(self, word):
        traverse = self.root
        for c in word:
            if c not in traverse:
                return False
            traverse = traverse[c]
        return 'END' in traverse


    def startsWith(self, prefix):
        traverse = self.root
        for c in prefix:
            if c not in traverse:
                return False
            traverse = traverse[c]
        return True
