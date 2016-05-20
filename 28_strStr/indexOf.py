class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None:
            return -1
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1