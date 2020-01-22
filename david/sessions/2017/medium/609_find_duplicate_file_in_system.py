class Solution(object):
    def findDuplicate(self, paths):
        d = {}
        result = []
        for path in paths:
            l = path.split()
            directory = l[0]
            for i in xrange(1, len(l)):
                l2 = l[i].split('(')
                name = l2[0]
                content = l2[1][:-1]

                if content not in d:
                    d[content] = []
                d[content].append('{}/{}'.format(directory, name))
        for key in d:
            if len(d[key]) > 1:
                result.append(d[key])
        return result
