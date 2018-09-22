class Solution(object):
    def find_root(self, trie, word):
        traverse = trie
        for c in word:
            if c not in traverse:
                break
            traverse = traverse[c]
            if 'END' in traverse:
                return traverse['END']
        return word

    def replaceWords(self, dict, sentence):
        trie = {}
        for word in dict:
            traverse = trie
            for c in word:
                if c not in traverse:
                    traverse[c] = {}
                traverse = traverse[c]
            traverse['END'] = word
        return ' '.join([self.find_root(trie, word) for word in sentence.split()])
