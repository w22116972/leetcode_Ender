class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        else:
            s = s.lower()
            i = 0
            j = len(s) - 1
            while(i < j):
                while(not s[i].isalnum() or not s[j].isalnum()):
                    if i == j:
                        break
                    elif not s[i].isalnum():
                        i += 1
                    else:
                        j -= 1
                if i >= j:
                    break
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True