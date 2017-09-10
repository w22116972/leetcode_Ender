class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 0
        prog = 10
        for i in range(len(digits)):
            total += digits[i] * pow(10, len(digits) - i - 1)
        total += 1
        total_str = str(total)
        ret_list = []
        for i in total_str:
            ret_list.append(int(i))
        return ret_list