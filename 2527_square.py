'''
2시간30분이라,,,
'''

def eval(grid):                 # 두번째 x2, y2랑 p1, q1비교
    if grid[4] > grid[2]:       # x2> p1 비교
        a = 0
    elif grid[4] == grid[2]:    # x2 = p1
        a = 1
    elif grid[6] == grid[0]:    # p2 = x1
        a = 2
    elif grid[6] < grid[0]:     # p2 < x1
        a = 3
    else:
        a = 4                   # 나머지 모든 겹치는 경우

    # y2랑 q2 비교
    if grid[5] > grid[3]:       # y2 > q1(안겹침)
        b = 0
    elif grid[5] == grid[3]:    # y2 = q1(점 or 선)
        b = 1
    elif grid[7] == grid[1]:    # q2 = y1
        b = 2
    elif grid[7] < grid[1]:     # q2 < y1
        b = 3
    else:                       # 나머지 모든 겹치는 경우
        b = 4

    return a, b

def answer(grid, code):
    if code[0] == 0 or code[1] == 0 or code[0] == 3 or code[1] == 3:
        return 'd'
    elif code[0] == 1 or code[0] == 2:
        if code[1] == 4:          # 오왼 선분
            return 'b'
        else:
            return 'c'            # 모든 꼭짓점
    elif code[0] == 4:
        if code[1] == 4:
            return 'a'            # 겹겹
        else:
            return 'b'            # 위아래 선분

for T in range(4):
    lst = list(map(int, input().split()))
    print(answer(lst, eval(lst)))