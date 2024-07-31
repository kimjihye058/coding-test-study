def solution(strArr):
    answer = []
    
    for idx, val in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(val.lower())
        else:
            answer.append(val.upper())
    
    return answer