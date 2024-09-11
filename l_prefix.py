#find the longest common prefix, if it doesnt exit print null, solve in linear time

def l_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs)
    longest = max(strs)
    for i, ch in enumerate(shortest):
        if ch != longest[i]:
            return shortest[:i]
    return shortest
