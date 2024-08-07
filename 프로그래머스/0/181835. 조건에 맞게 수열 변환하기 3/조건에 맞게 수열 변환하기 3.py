def solution(arr, k):
    answer = []
    if k % 2 == 0:
        answer = [num + k for num in arr]
    else:
        answer = [num * k for num in arr]
    return answer