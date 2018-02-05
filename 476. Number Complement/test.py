
def brute_force(num):
    b = ''
    while num > 0:
        if num % 2 == 0:
            b += '1'
        else:
            b += '0'
        num = int(num / 2)
    b = b[::-1]
    res = 0
    # binary with string type to decimal with integer type
    for i in range(len(b)):
        res += int(b[i]) * pow(2, (len(b)-1-i))
    return res


def test(f):
    assert f(5) == 2
    assert f(1) == 0
    assert f(2) == 1

test(brute_force)
# brute_force(2)

# b = '01'
# res = 0
# for i in range(len(b)):
#     # print(b[i])
#     res += int(b[i]) * pow(2, (len(b)-1-i))
# print(res)