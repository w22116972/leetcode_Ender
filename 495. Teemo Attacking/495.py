def findPoisonedDuration(timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    if len(timeSeries) == 0:
        return 0
    total = 0
    pre = timeSeries[0]
    while timeSeries:
        current = timeSeries.pop(0)
        if current - pre + 1 > duration:
            total += duration
        else:
            total += current - pre
        pre = current
    total += duration
    return total

print(findPoisonedDuration([1, 4], 2))

print(findPoisonedDuration([1, 2], 2))

