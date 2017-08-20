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

def single_number_set(nums):
    return 2 * sum(set(nums)) - sum(nums)


# Dict approach
def single_number_dict(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]

# List approach
def single_number_list(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        test = []
        for i in nums:
            if i not in test:
                test.append(i)
            else:
                test.remove(i)
        return test.pop()


if __name__ == "__main__":
    assert single_number_list([1,1,2,3,3]) == 2
    assert single_number_set([1,1,2,3,3]) == 2
    assert single_number_xor([1,1,2,3,3]) == 2
    assert single_number_dict([1,1,2,3,3]) == 2

