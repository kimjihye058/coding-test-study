def solution(myString):
    temp = myString.split('x')
    return [len(i) for i in temp]