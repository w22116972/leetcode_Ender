class Solution(object):
    def convertToTitle(self, n):
        s = ''
        while n > 0:
            n -= 1
            ch = n % 26 + 65
            n = int(n/26)
            s += chr(ch)
        return s[::-1]