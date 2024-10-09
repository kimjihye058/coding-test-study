def solution(my_string, indices):
    answer = [i for i in my_string]
    indices.sort()
    indices.reverse()
    for j in indices :
        del answer[j]
    return "".join(answer)