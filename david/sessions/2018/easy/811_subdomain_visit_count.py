class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for cpd in cpdomains:
            parts = cpd.split()
            count = int(parts[0])
            domain_parts = parts[1].split('.')
            l = len(domain_parts)
            for i in xrange(l):
                k = '.'.join(domain_parts[i:])
                d[k] = count if k not in d else d[k] + count
        return ['{} {}'.format(str(d[k]), k) for k in d]
