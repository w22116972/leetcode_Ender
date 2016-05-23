class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sp = s.strip().split(" ")
        ans = ""
        for i in range(len(sp) - 1, -1, -1):
            if sp[i] is "":
                continue
            else:
                ans += sp[i]
                if i > 0:
                    ans += " "
        return ans