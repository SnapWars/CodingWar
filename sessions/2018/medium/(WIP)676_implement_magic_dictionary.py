class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            cur = self.d
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['end'] = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        deviations = 0
        cur = self.d
        print self.d
        l = len(word)
        for i in xrange(l):
            c = word[i]
            if 'end' in cur:
                break
            if c not in cur:
                deviations += 1
                if deviations > 1:
                    return False

                return self.search_helper(word[i+1:], cur)
            else:
                cur = cur[c]

        return deviations == 1

    def search_helper(self, word, root):
        l = len(word)
        for k in root.keys():
            cur = root[k]
            for i in xrange(l):
                c = word[i]
                if c in cur:
                    cur = cur[c]
            if 'end' in cur:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
