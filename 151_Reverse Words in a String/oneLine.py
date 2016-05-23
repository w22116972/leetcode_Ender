class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # strip() can be removed since split() will handle beginning and ending spaces
        # ' '.join(split()) can remove duplicated spaces
        return ' '.join(reversed(s.split()))