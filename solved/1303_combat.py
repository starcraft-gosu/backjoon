'''
bfs로 풀어보자
visited 만들어서 한번 간 곳은 다시 가기 x
좌표마다 bfs 돌아버렷
각 좌표를 for문으로 돌며
더 갈데 없으면 인접한 횟수 출력 씥
델타 탐색으로 써칭
bfs를 함수로 구현하는게 나앗겟다
'''
from collections import deque

dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

N, M = map(int, input().split())
combat = list(input() for _ in range(M) )

visited = [[0] * N for _ in range(M)]
q = deque()             # 큐 생성
total_w = 0             # w팀 합
total_b = 0             # b팀 합

for i in range(M):
    for j in range(N):
        if visited[i][j]:   # visited == 1
            continue

        team = combat[i][j]             # 최초 좌표의 팀
        cnt = 1                         # cnt 생성
        q.append((i, j))                # 현재 좌표 큐에 저장
        visited[i][j] = 1

        # 큐에서 좌표를 뽑고 다시 bfs를 돌리기 & 횟수 체크
        while q:                        # 큐가 안비어잇으면
            y, x = q.popleft()          # 끄집어내서
            for dx, dy in dxy:          # 델타탐색
                ny, nx = y+dy, x+dx     # 현재좌표는 pop한애들 + 델타탐색
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue # 인덱스가 넘어가면
                if visited[ny][nx]: continue            # visited = 1이면

                if combat[ny][nx] == team:# team이랑 같을때
                    q.append((ny, nx))      # 현재좌표 애들 추가
                    cnt += 1
                    visited[ny][nx] = 1
        if team == 'W':
            total_w += cnt**2
        else:
            total_b += cnt**2

print(total_w, total_b)

# for (r,c) in dxy:
#     ny, nx = y+r, x+c   # 델타탐색
#     if combat[ny][nx] == team:  # 팀이 같으면
#         q.append((ny, nx))      # 큐에 추가
#         visited[nx][ny] = 1     # visited 추가
# while q:
#     popleft()

