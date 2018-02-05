def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    s_list = [i for i in s]
    vowels_rev = []
    vowel = 'aeiouAEIOU'
    for i in range(len(s_list)):
        if s_list[i] in vowel:
            vowels_rev.append(s_list[i])
            s_list[i] = 0
    for i in range(len(s_list)):
        if s_list[i] == 0:
            s_list[i] = vowels_rev.pop()
    return ''.join(s_list)

assert reverseVowels('hello') == 'holle'
assert reverseVowels('leetcode') == 'leotcede'
