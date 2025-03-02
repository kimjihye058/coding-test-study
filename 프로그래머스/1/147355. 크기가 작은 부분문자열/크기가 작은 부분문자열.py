def solution(t, p):
    # p를 숫자로 변환
    p_int = int(p)
    
    # t의 길이에서 p의 길이를 빼고, 그 만큼 반복하면서 부분 문자열을 체크
    count = 0
    for i in range(len(t) - len(p) + 1):
        # 부분 문자열을 숫자로 변환하여 비교
        if int(t[i:i+len(p)]) <= p_int:
            count += 1
    
    return count
