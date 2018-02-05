def brute_force(x, y):
    # convert decimal+intger to binary+string
    y_bin_str = int_to_bin_1(y)
    x_bin_str = int_to_bin_2(x)
    # filled with leading zeros
    while len(y_bin_str) != len(x_bin_str):
        if len(y_bin_str) < len(x_bin_str):
            y_bin_str = '0' + y_bin_str
        elif len(y_bin_str) > len(x_bin_str):
            x_bin_str = '0' + x_bin_str
    # compare different bits
    dif_bit_num = 0
    for i in range(len(x_bin_str)):
        if x_bin_str[i] != y_bin_str[i]:
            dif_bit_num += 1
    return dif_bit_num


def xor(x, y):
    x_xor_y = x ^ y
    return get_ones_count(x_xor_y)


def get_ones_count(x):
    '''
    every time you perform the operation x & (x-1), a single 1 bit is erased
    '''
    total = 0
    while x != 0:
        x = x & (x-1)
        total += 1
    return total


def int_to_bin_2(i):
    if i == 0:
        return "0"
    i_str = ''
    while i > 0:
        if i % 2 == 1:
            i_str = '1' + i_str
        else:
            i_str = '0' + i_str
        i = int(i / 2)
    return i_str


def int_to_bin_1(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i = int(i/2)
    return s


def dec_to_bin(i):
    s = ''
    t = {'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}
    for c in oct(i)[2:]:
        s += t[c]
    return s
print(dec_to_bin(5))