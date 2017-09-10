
def brute_force(n):
    b = ''
    while n > 0:
        if n % 2 == 0:
            b += '1'
        else:
            b += '0'
        n = int(n / 2)
    print(b)
    res = 0
    for i in range(len(b)):
        res += int(b[i]) * pow(2, (len(b)-1-i))
    return res


print(brute_force(5))
print(brute_force(1))
print(brute_force(2))

    


