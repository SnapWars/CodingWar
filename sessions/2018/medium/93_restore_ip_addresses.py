class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.l = len(s)
        self.result = []
        if self.l > 12:
            return self.result

        self.helper(s, 4)
        return self.result

    def helper(self, s, count, parts=[]):
        cur = None
        l = len(s)
        for i in xrange(l):
            c = s[i]
            if not cur:
                cur = c
            else:
                cur += c

            rem = l - (i+1)
            cur_i = int(cur)
            if 0 <= cur_i <= 255 and rem <= 3*(count-1):
                copy = list(parts)
                copy.append(cur)
                if rem == 0 and len(copy) == 4:
                    leading = False
                    for n in copy:
                        if len(str(int(n))) != len(n):
                            leading = True
                            break
                    if not leading:
                        self.result.append('.'.join(copy))
                else:
                    self.helper(s[i+1:], count-1, copy)
            elif cur_i > 255:
                return
