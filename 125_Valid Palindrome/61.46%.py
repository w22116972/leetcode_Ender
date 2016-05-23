class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = filter(lambda x: x.isalnum(), s.lower())
        return l == reversed(l)