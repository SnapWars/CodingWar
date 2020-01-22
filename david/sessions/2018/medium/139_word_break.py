class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.d = wordDict
        self.memo = {}
        return self.helper(s)

    def helper(self, s):
        if s in self.memo:
            return self.memo[s]
        cur = ''
        l = len(s)
        for i in xrange(l):
            cur += s[i]
            if cur in self.d:
                if self.helper(s[i+1:]):
                    self.memo[s[i+1]] = True
                    return self.memo[s[i+1]]
        self.memo[s] = cur in self.d
        return self.memo[s]

        '''
        Naive implementation (would be incorrect since greedy doesn't always work)
        '''
        '''
        cur = ''
        l = len(s)
        for c in s:
            cur += c
            if cur in wordDict:
                cur = ''
        return cur == ''
        '''
