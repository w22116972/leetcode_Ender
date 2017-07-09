
def merge3(nums1, m, nums2, n):
    '''
    
    '''
    for i in range(m+n-1, -1, -1):
        if m <= 0:
            n -= 1
            nums1[i] = nums2[n]
        elif n <= 0:
            break
        elif nums1[m-1] < nums2[n-1]:
            n -= 1
            nums1[i] = nums2[n]
        else:
            m -= 1
            nums1[i] = nums1[m]
    return nums1


def merge2(nums1, m, nums2, n):
    '''
    append nums2 to nums1 then sort nums1
    '''
    for i in range(n):
            nums1[m + i] = nums2[i]
    nums1.sort()
    return nums1


if __name__ == "__main__":
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(merge([0], 0, [1], 1))
    assert merge([0], 0, [1], 1) == [1]
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]

