'''
1,2,3번을 재귀함수로 만듦
조건은 if true로
1번 청소 후 2로 두기
2번은 if true 다 통과하면 d에따라 1, 2따지기
3번은 재귀 or while
d를 원형큐로 관리해도 되겟다
달팽이 공부하자
'''

dy = [-1, 0, 1, 0]  # 12시부터 시계방향
dx = [0, 1, 0, -1]

def rotate(direction):
    if direction == 0:
        direction = 3
    else:
        direction -= 1
def clean():
    room[y][x] = 2# 현재 칸 2로 만듦
    for _ in range(4):
        if not room[y+dy][x+dx]:
            rotate()
        break
    else:


N, M = map(int, input().split())
r, c, d = map(int, input().split())         # r, c는 인덱스로 쓸때 -1해야
room = [list(map(bool, input().split())) for _ in range(N)]
