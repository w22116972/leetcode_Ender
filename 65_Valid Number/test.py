'''
A string could be divided into these four substrings in the order from left to right:
s1. Leading whitespaces (optional).
s2. Plus (+) or minus (–) sign (optional). 
s3. Number.
    - whole number
    - decimal number
        a. Integer part
        b. Decimal point
        c. Fractional part
s4. Optional trailing whitespaces (optional).

'''


def isNumber_clean(s):
    i = 0
    n = len(str(s))
    # passing leading zeros
    while i < n and s[i] == ' ':
        i += 1
    # passing sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        i += 1
    is_num = False
    # procss of integer part
    while i < n and s[i].isdigit():
        i += 1
        is_num = True
    # encounter decimal point
    if i < n and s[i] == '.':
        i += 1
        # process of fractional part 
        while i < n and s[i].isdigit():
            i += 1
            is_num = True
    # encounter exponent part
    # "-1.2e+10", "+1.2e-10"
    if is_num and i < n and s[i] == 'e':
        i += 1
        is_num = False  # 不可以只有e沒有數字在後面
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1
        while i < n and s[i].isdigit():
            i += 1
            is_num = True
    # passing ending zeros
    while i < n and s[i] == ' ':
        i += 1
    # 在passing數字的過程中，如果遇到不ok的字元
    # is_num仍為True，因此最後要確保跟著走到底
    # 才會是每個字元都是數字 i.e. i == n
    return is_num and i == n


def isNumber_fsm(s):
        """
        :type s: str
        :rtype: bool
        
        Using Finite State Machine
        s0: white space
        s1: sign part
        s2: int part
        s3: decimal point
        s4: float part
        s5: exponential
        
        int: s0 -> s1 -> s2 -> s0
        float: s0 -> s1 -> s2 -> s3 -> s4 -> s0
        exp: s0 -> s1 -> s2 -> s5 -> s1 -> s2 -> s0
        """
        state = 0
        s = str(s)
        i = 0
        n = len(s)

        # State 0: Leading White Space
        while state == 0:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+' or s[i] == '-':
                i += 1
                state = 1
            elif s[i].isdigit():
                i += 1
                state = 2
            elif s[i] == '.':
                i += 1
                state = 3
            else:
                return False
        
        # State 1: Sign part
        if state == 1:
            if s[i].isdigit():
                i += 1
                state = 2
            elif s[i] == '.':
                i += 1
                state = 3
        
        # State 2: Integer part
        if state == 2:
            while i < n and s[i].isdigit():
                i += 1
            if s[i] == '.':
                i += 1
                state = 3
            elif s[i] == 'e':
                i += 1
                state = 5
        
        # State 3: Decimal Point 
        # 後面可接 e, float part
        if state == 3:
            if s[i] == 'e':
                i += 1
                state = 5
            elif s[i].isdigit():
                i += 1
                state = 4
            else:
                return False
        
        # State 4: Float part
        if state == 4:
            if s[i] == 'e':
                i += 1
                state = 5
            elif s[i].isdigit():
                while i < n and s[i].isdigit():
                    i += 1
                state = 0
        
        # State 5: Expoential part
        if state == 5:
            while i < n and s[i].isdigit():
                i += 1
            state = 0
        
        




                
