import re


def atoi(s):
    max_div10 = 2147483647 / 10
    max_int = 2147483647
    min_int = -2147483648
    i = 0
    s_len = len(s)
    while i < s_len and s[i] == ' ': 
        i += 1
    sign = 1
    if i < s_len and s[i] == '+':
        i += 1
    elif i < s_len and s[i] == '-':
        sign = -1
        i += 1
    num = 0
    while i < s_len and s[i].isdigit():
        digit = int(s[i])
        if num > max_div10 or num == max_div10 and digit >= 8:
            return max_int if sign == 1 else min_int
        num = num * 10 + digit
        i += 1
    return sign * num


def atoi_reg(s):
    '''
    THIS SOLUTION IS NOT OK
    The string can contain additional characters after those that form the integral number, 
    which are ignored and have no effect on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, 
    or if no such sequence exists because either str is empty or it contains only whitespace characters, 
    no conversion is performed.
    If no valid conversion could be performed, a zero value is returned. 
    If the correct value is out of the range of representable values, 
    the maximum integer value (2147483647) or the minimum integer value (–2147483648) is returned.
    '''
    s = str(s).rstrip()
    print(s)
    s = re.findall(r'^[+-]?\d+', s)
    try:
        res = int(''.join(s))
        max_int = 2147483647
        min_int = -2147483648
        if res > max_int:
            return max_int
        if res < min_int:
            return min_int
        return res
    except:
        return 0

print(atoi('   010'))