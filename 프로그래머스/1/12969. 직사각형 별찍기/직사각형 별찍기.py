n, m = map(int, input().strip().split())  # n은 가로 길이, m은 세로 길이

# m번 반복하며 가로 n만큼 별을 출력
for _ in range(m):
    print('*' * n)
