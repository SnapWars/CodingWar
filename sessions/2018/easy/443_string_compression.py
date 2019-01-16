class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev = None
        l = len(chars)
        i = l - 1
        count = 0
        while i >= 0:
            c = chars[i]
            if not prev:
                prev = c
                count = 1
            elif c != prev:
                if count > 1:
                    chars[i+1:i+1+count] = [prev] + list(str(count))
                prev = c
                count = 1
            else:
                count += 1
            i -= 1
        if count > 1:
            chars[i+1:i+1+count] = [prev] + list(str(count))
        return len(chars)
