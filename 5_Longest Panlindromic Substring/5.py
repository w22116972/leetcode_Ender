def brute_force(s):
    """
    :type s: str
    :rtype: str
    """
    longest_s = 0
    longest_i, longest_j = 0, 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if is_palindrom(s, i, j) and j - i + 1 > longest_s:
                longest_s = j - i + 1
                longest_i = i
                longest_j = j
    return s[longest_i:longest_j + 1]


def dp(s):
    '''
    P[i, j] is True iff s[i]~s[j] is palindromic  
    P[ i, j ] <- ( P[ i+1, j-1 ] and Si == Sj )

    Base Case:
        P[i, i] is True
        P[i, i+1] <- s[i] = s[i] + 1
    '''
    pass


def expand_from_center(s):
    longest_len = 0
    longest_i = -1
    longest_j = -1
    for d in range(0, len(s) - 1):
        # Case 1: center is single digit
        if d - 1 > 0 and d + 1 <= len(s):
            print("Entering Case 1")
            i = d - 1
            j = d + 1
            while s[i] == s[j]:
                if i - 1 > 0 and j + 1 <= len(s):
                    i += 1
                    j += 1
                else:
                    break
            if j - i + 1 > longest_len:
                longest_len = j - i + 1
                longest_i, longest_j = i, j
            print(longest_i, longest_j)
        # Case 2: center is double digit e.g. baab
        if d + 1 != len(s) and s[d] == s[d + 1]:
            print("Entering Case 2")
            i = d
            j = d + 1
            while s[i] == s[j]:
                if i - 1 >= 0 and j + 1 <= len(s):
                    i += 1
                    j += 1
                else:
                    break
            if j - i + 1 > longest_len:
                longest_len = j - i + 1
                longest_i, longest_j = i, j
            print(longest_i, longest_j)
    print(longest_len)
    print(s[longest_i:longest_j + 1])
    return s[longest_i:longest_j + 1]


def expand_from_center_clean(s):
    """
    |center is single digit| = O(n) because there are |n| digits.
    |center is double digits| = O(n-1) because (1,2) ~ (n-1,n) is |n-1|
    Total center is |2n-1| = O(2n) = O(n)
    T(Expand from center) = O(n/2) = O(n)
    Total time complexity = O(n) * O(n) = O(n^2)
    """
    start = 0
    end = 0
    for i in range(len(s)):
        len_single_center = expand_from_center(s, i, i)
        len_double_center = expand_from_center(s, i, i + 1)
        len_max = max(len_single_center, len_double_center)
        if len_max > end - start:
            start = i - int((len_max - 1) / 2)
            end = i + int(len_max / 2)
    # print(start, end, len_max)
    # print(s[start:end + 1])
    return s[start:end + 1]


def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

    


def is_palindrom(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    if i == j:
        if s[i] == s[j]:
            return True
        else:
            return False
    return True

# print(brute_force("babad"))
assert brute_force("babad") == "bab"
assert brute_force("cbbd") == "bb"

# print(expand_from_center("babad"))
# assert expand_from_center("babad") == "bab" or "aba"
# assert expand_from_center("cbbd") == "bb"

# assert expand_from_center_clean("babad") == "bab" or "aba"
assert expand_from_center_clean("cbbd") == "bb"
print(expand_from_center_clean("abacdfgdcaba"))
