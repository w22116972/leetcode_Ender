def reverse_word(s):
    '''
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    '''
    s = str(s)
    word = s.split(' ')
    result = ''
    for w in word:
        result = result + w[::-1] + ' '
    return result[:-1]


def reverse_word1(s):
    return ' '.join(x[::-1] for x in s.split())

print(reverse_word('Let\'s take LeetCode contest'))
print(reverse_word1('Let\'s take LeetCode contest'))