class Solution(object):
    def detectCapitalUse(self, word):
        return (word == word.upper()) or (word == word.lower()) or (word[0] == word[0].upper() and word[1:] == word[1:].lower())
