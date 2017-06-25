def lengthOfLongestSubstring(s):
    '''
    We have to find a maximal substring with only distinct digits.
    So We can use variable length array as a substring for answer.
    Then we start to loop given string.
    If current value in this iteration is new to substring array,
    we can put this value into array.
    And update maximal length if current length of substring is greater than maximal length.
    If current value is already in this substring,
    we have to restart the new substring by deleting current substring and add current value into new substring.
    '''
    max_len = 0
    substring = []
    for i in range(0, len(s)):
        if s[i] not in substring:
            substring.append(s[i])
            max_len = max(len(substring), max_len)
        else:
            max_len = max(len(substring), max_len)
            start_idx = substring.index(s[i])
            del substring[0:start_idx + 1]
            substring.append(s[i])
    return max_len


def lengthOfLongestSubstring_dp(s):
    '''
    1) If s[i] is not in the current char_index,
    then we add s[i + 1] into char_index and L[i + 1] = s[start_index...i + 1]


    2) If s[i] is already in the char_index,
    we can use max function to set s[i] as the start_index.

    e.g start_index = max(start_index, char_index[s[i + 1]])

    '''
    max_len = 0
    start_index = 0
    char_index = {i: -1 for i in range(1, 257)}
    for i in range(len(s)):
        start_index = max(char_index[ord(s[i])] + 1, start_index)
        char_index[ord(s[i])] = i
        max_len = max(max_len, i - start_index + 1)
    return max_len


def lengthOfLongestSubstring_1(self, s):
        start = maxLength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

assert(lengthOfLongestSubstring_dp("abcabcbb") == 3)
assert(lengthOfLongestSubstring_dp("bbbbb") == 1)
assert(lengthOfLongestSubstring_dp("pwwkew") == 3)
assert(lengthOfLongestSubstring_dp("c") == 1)
assert(lengthOfLongestSubstring_dp("dvdf") == 3)
assert(lengthOfLongestSubstring_dp("dvfed"))

# print(lengthOfLongestSubstring_one_iter("abcabcbb"))
# print(lengthOfLongestSubstring_one_iter("bbbbb"))
# print(lengthOfLongestSubstring_one_iter("pwwkew"))