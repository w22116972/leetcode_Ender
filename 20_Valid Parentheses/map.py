def isValid(s):
    stack = []
    right_to_left = {')':'(',']':'[','}':'{'}
    for c in s:
        if stack and c in right_to_left.keys() and stack.pop() != right_to_left[c]:  # c is right parenthese
            return False
        elif c in right_to_left.values():  # c is left parenthese
            stack.append(c)
        else:  # c is not one of them
            return False
    return stack == []


assert isValid('()[]') == True
assert isValid('[()]') == True
assert isValid('[(])') == False
