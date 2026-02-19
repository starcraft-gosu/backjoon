'''
l <= p <= r
이면 하나로 묶고
평균으로 퉁치기(소수점 퉤)
0. while로 연합 안될때까지 돌리기?
1. 날짜별 연합 함수 만들기
    연합별 좌표 관리
    계산한 인구를 좌표에 때려박고 종료
2. 이동 여부 return 0 or 1
3. 최종 횟수 return
'''
import sys
input = sys.stdin.readline



def immigration(n, l, r, arr):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[0]*n for i in range(n)]


    unite = 0   # 연합개수
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            stack = []
            stack.append((i, j))
            unite += 1
            visited[i][j] = unite
            pointer = 0
            num_p = 0

            # 연합 묶기
            while pointer < len(stack):
                cy, cx = stack[pointer]
                num_p += arr[cy][cx]
                for k in range(4):
                    ny, nx = cy+dy[k], cx+dx[k]
                    if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                        dif = arr[cy][cx] - arr[ny][nx]
                        if l <= abs(dif) <= r:
                            stack.append((ny, nx))
                            visited[ny][nx] = unite
                pointer += 1
            # print(stack)
            new_p = num_p // len(stack)
            for y, x in stack:
                arr[y][x] = new_p
    if unite < n*n:
        return 1
    else:
        return 0

def how_long():
    n, l, r = map(int, input().split())

    popul = [list(map(int, input().split()))  for i in range(n)]
    # print(popul)
    ans = 0
    while immigration(n, l, r, popul):
        ans += 1
    return ans
print(how_long())