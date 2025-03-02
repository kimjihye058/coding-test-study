def solution(A, B):
    A.sort()  # A는 오름차순 정렬
    B.sort(reverse=True)  # B는 내림차순 정렬
    return sum(a * b for a, b in zip(A, B))
