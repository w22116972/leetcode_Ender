def lengthOfLongestSubstring(s):
    '''
    
    '''
    max_len = 0
    queue = []
    for i in range(0, len(s)):
        if s[i] not in queue:
            queue.append(s[i])
            if len(queue) > max_len:
                max_len = len(queue)
        else:
            if len(queue) > max_len:
                max_len = len(queue)
            start_idx = queue.index(s[i])
            del queue[0:start_idx + 1]
            queue.append(s[i])
    return max_len


assert(lengthOfLongestSubstring("abcabcbb") == 3)
assert(lengthOfLongestSubstring("bbbbb") == 1)
assert(lengthOfLongestSubstring("pwwkew") == 3)
assert(lengthOfLongestSubstring("c") == 1)
assert(lengthOfLongestSubstring("dvdf") == 3)
assert(lengthOfLongestSubstring("dvfed"))
 
# print(lengthOfLongestSubstring_one_iter("abcabcbb"))
# print(lengthOfLongestSubstring_one_iter("bbbbb"))
# print(lengthOfLongestSubstring_one_iter("pwwkew"))