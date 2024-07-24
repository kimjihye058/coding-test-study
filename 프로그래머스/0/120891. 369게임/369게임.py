def solution(order):
    answer = str(order).count("3") + str(order).count("6") + str(order).count("9")
    return answer