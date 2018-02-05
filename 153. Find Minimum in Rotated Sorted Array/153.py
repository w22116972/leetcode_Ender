"""
已排序的旋轉陣列, 任取一點M, 只有兩種情形:
1. 最低點的左邊(所有值皆大於右邊) 2. 最低點(含)的右邊(所有值都小於左邊)
先取陣列的中點m跟left和right比較
情況1: m > right
    -> 最低點位在m的右邊
    -> m的左邊都不用考慮
    -> 取left = m + 1把範圍切成m+1 ~ right
情況2: m < right
    -> 最低點位在m的左邊
    -> m的右邊都不用考慮
    -> 取right = m把範圍切成left ~ m
持續切中點m比較, 直到left == right

"""


def find_min(a):
    """
    T = O(log n) because everytime we divide array into half.
    """
    left, right = 0, len(a) - 1
    while left < right and a[left] >= a[right]:
        m = int((left + right) / 2)
        if a[m] > a[right]:  # case 1
            left = m + 1
        else:  # case 2
            right = m
    return a[left]  # now left == right


def brute_force(a):
    """
    T = O(n)
    """
    m = a[0]
    for val in a[1:]:
        if val < m:
            m = val
    return m
