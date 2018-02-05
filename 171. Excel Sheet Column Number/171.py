class Solution(object):
    def titleToNumber(self, s):
        if len(s) == 1:
            return ord(s)-64
        s_rev = s[::-1]
        total = 0
        for i in range(len(s)):
            total += (ord(s_rev[i])-64) * pow(26, i)
        return total