class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for e in emails:
            l, d = e.split('@')
            s = l.split('+')
            result.add(''.join(s[0].split('.')) + '@' + d)
        return len(result)
