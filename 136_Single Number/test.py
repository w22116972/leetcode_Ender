def single_number_xor(nums):
    '''
    We see all numbers as binary format(using bitwise xor)
    The two same numbers xor each other will give 0
    e.g. 0 xor a xor a xor b xor c xor c = 0 xor b = b
    ^ is bitwise for xor
    '''
    a = 0
    for i in nums:
        a ^= i
    return a




