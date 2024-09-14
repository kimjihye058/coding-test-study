def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        if numLog[i]-numLog[i-1] == 1:
            answer +='w'
        elif numLog[i]-numLog[i-1] == -1:
            answer +='s'
        elif numLog[i]-numLog[i-1] == 10:
            answer +='d'
        elif numLog[i]-numLog[i-1] == -10:
            answer +='a'
        else:
            continue
    return answer