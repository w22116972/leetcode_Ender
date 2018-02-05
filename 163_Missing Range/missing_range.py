def find_missing_ranges(vals):
    ranges = []
    start = 0
    end = 99
    if len(vals) == 0:
        return ["0->99"]
    elif len(vals) == 100:
        return []
    else:
        for i in range(len(vals)):
            if i == 0:
                if (vals[i] - 1) - start > 0:
                    ranges.append(str(start) + "->" + str(vals[i] - 1))
                elif (vals[i] - 1) == start:
                    ranges.append(str(start))
            elif i == len(vals) - 1:
                if end - (vals[i] + 1) > 0:
                    ranges.append(str(vals[i] + 1) + "->" + str(end))
                elif (vals[i] + 1) == end:
                    ranges.append(str(end))
            else:
                if (vals[i] - 1) - (vals[i - 1] + 1) > 0:
                    ranges.append(str(vals[i] - 1) + "->" + str(vals[i - 1] + 1))
                else:
                    ranges.append(str(vals[i] - 1))
    return ranges

find_missing_ranges([1, 3, 5, 7])


def find_missing_ranges_clean(vals):
    """
    目標是0~99所以設個-1和100來包住

    """
    ranges = []
    start, end = 0, 99
    prev = start - 1  # 從-1開始包
    for i in range(len(vals)+1):
        # else為100
        current = vals[i] if i != len(vals) else end + 1
        if current - prev >= 2:  # 需要->的情形(not consecutive)
            # 只取包住的情形
            ranges.append(get_range(prev+1, current-1))
        prev = current
    return ranges


def get_range(start, end):
    return str(start) if start == end else str(start) + "->" + str(end)

print(find_missing_ranges_clean([0, 1, 3, 50, 75]))
