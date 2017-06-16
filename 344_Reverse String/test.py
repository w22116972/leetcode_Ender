class Solution(object):
    def reverseString_pythonic(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverse_string_recur(self, s):
        word_len = len(s)
        if word_len < 2:
            return s
        return self.reverse_string_recur(s[word_len/2:]) + self.reverse_string_recur(s[:word_len/2])

    def reverse_string_swap(self, s):
        lst = list(s)
        i, j = 0, len(lst) - 1
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i++
            j++
        return "".join(lst)
