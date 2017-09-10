def roman_to_int_reverse(r):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    neg = False
    total = 0
    r = str(r)[::-1]
    for i in range(len(r)):
        if i == 0:
            total += roman_dict[r[i]]
        elif roman_dict[r[i]] < roman_dict[r[i-1]]:
            total -= roman_dict[r[i]]
        elif roman_dict[r[i]] >= roman_dict[r[i-1]]:
            total += roman_dict[r[i]]
    return total

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        current_digit = roman_dict[s[i]]
        if i + 1 < len(s):
            if roman_dict[s[i+1]] > current_digit:
                total -= current_digit
            else:
                total += current_digit
        else:
            total += current_digit
    return total

assert roman_to_int('III') == 3
assert roman_to_int('IV') == 4
assert roman_to_int('VIII') == 8
assert roman_to_int('XLVIII') == 48
assert roman_to_int('XCVIII') == 98
assert roman_to_int('XIX') == 19
assert roman_to_int('MDCLXVI') == 1666

