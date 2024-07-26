def solution(num, k):
    num=str(num)
    k=str(k)
    return -1 if k not in num else num.find(k)+1