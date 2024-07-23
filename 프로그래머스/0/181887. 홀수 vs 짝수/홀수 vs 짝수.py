def solution(num_list):
    A = 0
    B = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            A += num_list[i]
        else:
            B += num_list[i]
    if A > B:
        return A
    else:
        return B
