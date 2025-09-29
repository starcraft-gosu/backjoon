'''
다리 건설 조건 : x or y 좌표 같은거 & 두칸 이상 떨어져잇기 & 중간에 육지 없음
섬 조건 : 델타 상하좌우에 1 없기
섬 생성 : 섬을 x좌표랑 y좌표 구간으로 나눠야겟다 - 3<x<7, 4<y<8 이렇게 될라나
여까지 완성
섬 연결 : x 또는 y좌표가 같고 차가 1보다 크고 젤 적은것
섬이 모두 연결돼잇다? : 섬 연결 리스트 추가?
'''
'''
새로 안 사실 : scope 규칙으로 인해서 함수 인자에 안넣어준 놈도 볼수잇다.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # height, width
map_info = list(list(map(int, input().split())) for _ in range(N))
print(map_info)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited = [[0] * M for _ in range(N)]
print(visited)

def seek(y, x, N, M): # 1인걸 발견하면 고대로 섬 만드는 놈
    # visited가 0이고 map_info가 1이면
    if visited[y][x] == 1:
        return None
    else:
        visited[y][x] = 1
    stack = [(y, x)]
    land = []
    while stack:
        cy, cx = stack.pop()
        land.append((cy, cx))
        if map_info[cy][cx] == 1:
            for k in range(4):
                ny = cy + dy[k]
                nx = cx + dx[k]
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] != 1 and map_info[ny][nx] == 1:
                    stack.append((ny, nx))
                    visited[ny][nx] = 1
    return land


islands = []
for i in range(N):
    for j in range(M):
        if map_info[i][j] == 1:
            island = seek(i, j, N,  M)
            if island:
                islands.append(island)

print(islands, len(islands))

# 섬마다 연결 여부 확인
for i in range(len(islands - 1)):
    for j in range(i+1, len(islands)):
        # islands[i], island[j]비교
        a = islands[i]
        b = islands[j]
        # 가로 연결

        # 세로 연결

        pass