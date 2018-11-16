class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        strings = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        ]
        rows = [set(s) for s in strings]
        result = []
        for word in words:
            s = set(word.lower())
            for row in rows:
                if len(s.intersection(row)) == len(s):
                    result.append(word)
        return result
