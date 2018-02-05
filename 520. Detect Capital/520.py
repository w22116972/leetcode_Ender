class Solution(object):
    def detectCapitalUse(self, word):
        case1 = True
        case2 = True
        case3 = True
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if word[0] in upper_case:
            case2 = False
            for i in range(1, len(word)):
                if case1 and word[i] in lower_case:
                    case1 = False
                if case3 and word[i] in upper_case:
                    case3 = False
                if not case1 and not case3:
                    return False
            return case1 or case3
        else:
            case1 = False
            case3 = False
            for i in range(1, len(word)):
                if word[i] in upper_case:
                    # case2 = False
                    return False
            return case2  # case2 = True