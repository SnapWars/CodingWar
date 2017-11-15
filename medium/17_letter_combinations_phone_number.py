import itertools

class Solution(object):
    def __init__(self):
        self.mapping = {
            1: ['*'],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: [' ']
        }

    def letterCombinations(self, digits):
        l = []
        if not digits:
            return l
        d = map(int, digits)
        for digit in d:
            l.append(self.mapping[digit])
        l2 = list(itertools.product(*l))
        return [''.join(i) for i in l2]
