T = int(input())

for tc in range(T):
    M, N = map(int, input().split())
    print(M-1)
    flight = []
    for _ in range(N):
        flight.append(tuple(map(int, input().split())))
