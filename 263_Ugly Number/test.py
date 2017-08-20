def isUgly(num):
    if num < 0:
        return False
    while int(num) != 0 and int(num) % 2 == 0:
        num /= 2
    while int(num) != 0 and int(num) % 3 == 0:
        num /= 3
    while int(num) != 0 and int(num) % 5 == 0:
        num /= 5
    print(num)
    if int(num) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    assert isUgly(6) == True
    assert isUgly(8) == True
    assert isUgly(14) == False
    assert isUgly(-2147483648) == False