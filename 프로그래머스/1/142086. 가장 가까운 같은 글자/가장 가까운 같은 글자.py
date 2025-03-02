def solution(s):
    last_seen = {}
    result = []
    for i, char in enumerate(s):
        if char in last_seen:
            result.append(i - last_seen[char])
        else:
            result.append(-1)
        last_seen[char] = i 
    return result

