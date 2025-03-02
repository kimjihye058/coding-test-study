def solution(arr):
    result = []
    for num in arr:
        if not result or result[-1] != num:
            result.append(num)
    return result
