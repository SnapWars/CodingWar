class Solution(object):
    def findWords(self, words):
        result = []
        keyboard = [
            set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']),
            set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']),
            set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        ]

        for word in words:
            s = set(list(word.lower()))
            l = len(s)
            for row in keyboard:
                if l == len(s.intersection(row)):
                    result.append(word)

        return result
