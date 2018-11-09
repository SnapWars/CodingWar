class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {}
        for m in moves:
            d[m] = 1 if m not in d else d[m] + 1
        ver = True
        hor = True
        if 'U' in d and 'D' in d:
            ver = d['U'] == d['D']
        elif 'U' in d or 'D' in d:
            ver = False

        if 'L' in d and 'R' in d:
            hor = d['L'] == d['R']
        elif 'L' in d or 'R' in d:
            hor = False

        return ver and hor
