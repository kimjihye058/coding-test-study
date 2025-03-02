def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        if int(num ** 0.5) ** 2 == num:
            result -= num
        else:
            result += num
    return result
