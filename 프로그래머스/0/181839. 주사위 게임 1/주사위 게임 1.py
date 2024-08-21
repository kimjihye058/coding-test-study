def solution(a, b):
    answer = 0
    if a % 2 == 0 and b% 2 == 0:
        answer = abs(a - b)
    elif a % 2 != 0 and b % 2 != 0:
        answer = pow(a, 2) + pow(b, 2)
    else:
        answer = 2 * (a + b)
        
    return answer