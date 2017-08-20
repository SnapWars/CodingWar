class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r_count = {}
        m_count = {}
        r = set(ransomNote)

        for c in ransomNote:
            r_count[c] = 1 if c not in r_count else r_count[c] + 1

        for c in magazine:
            m_count[c] = 1 if c not in m_count else m_count[c] + 1

        for c in r:
            if c not in m_count or m_count[c] < r_count[c]:
                return False

        return True
