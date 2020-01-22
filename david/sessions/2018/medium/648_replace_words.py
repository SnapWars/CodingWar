class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        d = {'root': True}

        for k in dict:
            cur = d
            for c in k:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['end'] = True

        result = []
        for word in sentence.split():
            cur = d
            for i in xrange(len(word)):
                if 'end' in cur:
                    break
                if word[i] in cur:
                    cur = cur[word[i]]
                else:
                    break
            if 'root' in cur:
                result.append(word)
            elif 'end' not in cur:
                result.append(word)
            else:
                if i == 0:
                    result.append(word)
                else:
                    result.append(word[:i])
        return ' '.join(result)
