def solution(arr):
    cnt = 0
    while len(arr) != 2 ** cnt:
        if len(arr) == 2 ** cnt:
            break
        if len(arr) > 2 ** cnt:
            cnt += 1
        else:
            chan = (2 ** cnt) - len(arr)
            for _ in range(chan):
                arr.append(0)
    return arr