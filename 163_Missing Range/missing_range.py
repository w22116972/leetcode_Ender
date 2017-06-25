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
                    ranges.append(str(start) + "-" + str(vals[i] - 1))
                elif (vals[i] - 1) == start:
                    ranges.append(str(start))
            elif i == len(vals) - 1:
                if end - (vals[i] + 1) > 0:
                    ranges.append(str(vals[i] + 1) + "-" + str(end))
                elif (vals[i] + 1) == end:
                    ranges.append(str(end))
            else:
                if (vals[i] - 1) - (vals[i - 1] + 1) > 0:
                    ranges.append(str(vals[i] - 1) + "-" + str(vals[i - 1] + 1))
                else:
                    ranges.append(str(vals[i] - 1))
    print(ranges)

find_missing_ranges([1, 3, 5, 7])