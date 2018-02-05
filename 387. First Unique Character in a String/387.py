def first_unique_char(s):
    char_order = []
    char_to_index = {}
    for i in range(len(s)):
        if s[i] not in char_to_index:
            char_to_index[s[i]] = i
            char_order.append(s[i])
        elif s[i] in char_order:
            char_order.pop(char_order.index(s[i]))
    if len(char_order) <= 0:
        return -1
    return char_to_index[char_order.pop(0)]