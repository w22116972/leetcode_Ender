def groupAnagrams(strs):
    group = {}
    for s in strs:
        k = ''.join(sorted(s))
        if k not in group:
            group[k] = [s]
        else:
            group[k].append(s)
    return list(group.values())


def set_default(strs):
    groups = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        groups.setdefault(sorted_s, list())
        groups[sorted_s].append(s)
    return groups.values()


def collection_defaultdict(strs):
    group = collection_defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return map(sorted, group.values())


def f(strs):
    return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]


