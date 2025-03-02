def solution(n):
    count_ones = bin(n).count('1')  # n의 2진수에서 1의 개수
    next_num = n + 1  # n보다 큰 수부터 탐색

    while bin(next_num).count('1') != count_ones:
        next_num += 1  # 1의 개수가 같아질 때까지 증가

    return next_num