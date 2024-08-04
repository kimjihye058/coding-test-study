def solution(n):
    s = n ** (1/2)
    if s % 1 == 0:
        return 1
    else:
        return 2
