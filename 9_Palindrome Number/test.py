class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_s = str(x)
        return x_s == x_s[::-1]

    def isPalindrome_2(self, x):
        if x < 0:
            return False
        if x / 10 == 0:
            return True
        toS = x
        toB = 0
        while toS >= 10:
            toB *= 10
            toB += toS % 10
            toS /= 10

        return toB == x / 10
