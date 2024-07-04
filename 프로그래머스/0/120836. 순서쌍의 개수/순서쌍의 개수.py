def solution(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1  # (i, n//i)
            if i != n // i:
                count += 1  # (n//i, i) 중복을 피하기 위해 체크
    return count
