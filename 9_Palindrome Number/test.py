
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    x_s = str(x)
    return x_s == x_s[::-1]


def isPalindrome_1(x):
    if x < 0:
        return False
    if x / 10 == 0:
        return True
    remain = x
    reverse = 0
    while remain >= 10:
        reverse *= 10
        reverse += remain % 10
        remain = int(remain / 10)
    print(reverse)
    return reverse == int(x / 10)

def isPalindrome_str(x):
    if x < 0:
        return False
    if x / 10 == 0:
        return True
    x = str(x)
    n = len(x)
    for i in range(int(n/2)):
        if x[i] != x[n-i-1]:
            return False
    return True

def isPalindrome_divide_by_10(x):
    if x < 0:
        return False
    if x / 10 == 0:
        return True
    remain = x
    reverse = 0
    while remain >= 10:
        reverse *= 10
        reverse += remain % 10
        remain /= 10
    return reverse == x / 10


def isPalindrome_half(x):
    reverse = 0
    while x > reverse:
        # propagation
        reverse = reverse * 10
        # add right most reverse in x to reverse
        reverse += x % 10
        # shift x left
        x = int(x/ 10)
    # first case is for even number of digits
    # second case is for odd number of digits
    return x == reverse or  x == int(reverse / 10)


if __name__ == "__main__":
    assert isPalindrome_1(1) == True
    assert isPalindrome_1(56789) == False
    # assert isPalindrome_half(17771) == True # odd 
    # assert isPalindrome_half(22222) == True 
    # assert isPalindrome_half(56789) == False

