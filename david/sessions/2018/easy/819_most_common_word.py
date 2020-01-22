import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        b = set(banned)
        s = re.findall(r"[\w]+", paragraph)
        d = {}

        for w in s:
            lower = w.lower()
            if lower not in b:
                d[lower] = 1 if lower not in d else d[lower] + 1
        _max = max(d.values())
        for k in d:
            if d[k] == _max:
                return k
