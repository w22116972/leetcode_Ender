def intuition(num):
    # num_list = list(str(num))
    # # once = False
    # res = ''
    # for i in range(len(num_str)):
        
    # print(res)
    # return int(res)
    pass





def brute_force_str(num):
    num_list = list(str(num))
    num_max = num_list[:]
    for current_index in range(len(num_list)):
        for swap_index in range(current_index+1, len(num_list)):
            if int(num_list[swap_index]) > int(num_list[current_index]):
                num_list[swap_index], num_list[current_index] = num_list[current_index], num_list[swap_index]
                if int(''.join(num_list)) > int(''.join(num_max)):
                    num_max = num_list[:]
                num_list[swap_index], num_list[current_index] = num_list[current_index], num_list[swap_index]
    return int(''.join(num_max))

def hash_table(num):
    '''
    O(n) + O(n) + O(n) * O(9)
    '''
    num_list = list(str(num))
    digit_to_index = {digit: index for index, digit in enumerate(num_list)}
    # print(digit_to_index)
    for index, number in enumerate(num_list):
        # print(type(number))
        for digit in range(9, int(number), -1):
            if str(digit) in digit_to_index.keys() and digit_to_index[str(digit)] > int(index):
                num_list[index], num_list[digit_to_index[str(digit)]] = num_list[digit_to_index[str(digit)]], num_list[index]
                # print(int(''.join(num_list)))
                return int(''.join(num_list))
    # print(num)
    return num  

def brute_force_int(num):
    max_digit = 0
    max_index = -1
    current_index = 0
    swap_index1 = 0
    swap_index2 = 0
    num_from_least_list = []
    while num > 0:
        digit = num % 10
        num_from_least_list.append(digit)
        if max_digit > digit:
            swap_index1 = current_index
            swap_index2 = max_index
        elif digit > max_digit:
            max_digit = digit
            max_index = current_index
        num = int(num / 10)
        current_index += 1
    num_from_least_list[swap_index1], num_from_least_list[swap_index2] = num_from_least_list[swap_index2], num_from_least_list[swap_index1]
    total = 0
    for i in range(len(num_from_least_list)):
        total += (int)(num_from_least_list[i] * 10**i)
    return total

def dp(num):
    '''
    f(2736) => dp = [1, 1, 3, 3]
    f(1993) => dp = [2, 2, 2, 3]
    '''
    num_str = list(str(num))
    dp = [-1]*len(num_str)
    current_max_index = len(num_str)-1
    for i in range(len(num_str)-1, -1, -1):
        if num_str[i] > num_str[current_max_index]:
            current_max_index = i
        dp[i] = current_max_index
    for i in range(len(num_str)-1):
        if num_str[dp[i]] != num_str[i]:
            num_str[i], num_str[dp[i]] = num_str[dp[i]], num_str[i]
            break
    return int(''.join(num_str))

def test(f):
    assert f(2736) == 7236
    assert f(9973) == 9973
    assert f(98368) == 98863
    assert f(1993) == 9913

# dp(1993)
test(brute_force_str)
test(brute_force_int)
test(hash_table)
test(dp)