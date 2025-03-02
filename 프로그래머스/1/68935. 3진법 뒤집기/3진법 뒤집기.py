def solution(n):
    answer = ""
    while n > 0:
        answer = str(n % 3) + answer  # 3으로 나눈 나머지를 앞에 추가
        n = n // 3  # n을 3으로 나누어 갱신

    # 3진법 숫자를 뒤집기
    reversed_answer = answer[::-1]

    # 뒤집힌 3진법 숫자를 10진법으로 변환
    return int(reversed_answer, 3)
