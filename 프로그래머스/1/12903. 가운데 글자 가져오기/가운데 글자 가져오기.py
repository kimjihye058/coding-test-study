def solution(s):
    n = len(s)
    mid = n // 2 
    return s[mid] if n % 2 == 1 else s[mid - 1:mid + 1]


