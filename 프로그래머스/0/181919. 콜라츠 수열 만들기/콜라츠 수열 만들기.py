def solution(n):
    answer = [] 
    while n!=1:
        answer.append(int(n))
        if n%2==0:
            n/=2
        else:
            n=3*n+1
    answer.append(1)
    return answer