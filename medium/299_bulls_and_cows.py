class Solution(object):
    def getHint(self, secret, guess):
        result = {'A': 0, 'B': 0}
        count = {'s': {}, 'g': {}}
        s = map(int, list(secret))
        g = map(int, list(guess))

        for i in s:
            count['s'][i] = 1 if i not in count['s'] else count['s'][i] + 1
        for j in g:
            count['g'][i] = 1 if i not in count['g'] else count['g'][i] + 1
        
        for x, y in zip(s, g):
            if x == y:
                result['A'] += 1
                count['s'][x] -= 1
                count['g'][y] -= 1

        for k in count['s']:
            if k in count['g']:
                result['B'] += min(count['s'][k], count['g'][k])
        return '{}A{}B'.format(result['A'], result['B'])
