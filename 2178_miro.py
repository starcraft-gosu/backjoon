'''
잘 돌아다녀보자...
1. 바닥이 0이면 안되고 1이면 가는거야
2. 1이면 저장하고 visited 찍는거야
3. 저장할땐 몇칸 가는지도 찍는거야
4. pop햇는데 도착점이면 몇칸 갓는지 리스트에 넣는거야
5. 맥스 쓰지말고 비교해서 뽑아내자
'''
def DFS(n, m):
    stack = [(1, 1, 1)]     # x, y, cnt
    visited = [[0]*(m+1) for _ in range(n+1)]
    visited[1][1] = 1
    while stack:
        x, y, cnt = stack.pop()
        if x == m and y == n:
            distance.append(cnt)
        for i in range(len(dxy)):
            nx, ny = x+dxy[i][0], y+dxy[i][1]
            if miro[ny][nx] == 1 and visited[ny][nx] != 1:
                stack.append((nx, ny, cnt+1))
                visited[ny][nx] = 1


N, M = map(int, input().split())
miro = [[0]*(M+2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] +[[0]*(M+2)]      # 미로에 벽 둘러치기
print(miro)

dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
distance = []

DFS(N, M)
print(min(distance))