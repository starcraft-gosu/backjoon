'''
전기줄이 교차하는때는 한쪽은 크고 다른 쪽은 작을때
1,7 2,6
1. 전기줄 별로 교차점 배열 만들기 ex) 1번 = [2, 3, 4] 2번 = [3, 5]
2. 전기줄 교차점 개수별로 정렬
3. 교차점이 가장 많은 전기줄부터 하나씩 제거
4. 제거할때마다 교차점 개수(배열 길이)비교 하며 계속 진행

테케
0 - 한줄일때
1 - 아무것도 안만날때
2 - 한점에서 만날때
3 - 하나씩 교차할때
4 - 한점에서 만나는놈들 + 안만나는
4.1 - 한점에서 만나는놈들 X 2
'''
import sys
input = sys.stdin.readline

N = int(input())
lines = [0] * N
for i in range(N):
    lines[i] = tuple(map(int, input().split()))

# 자기를 제외하고 교차되는 줄 배열만들기
def cross(N):
    meets = [[] for _ in range(N)] # [[1, 3, 6], [0, 2, 5] ...]

    for curr_idx, curr_line in enumerate(lines):
        for idx, line in enumerate(lines):
            # 교차하는 두가지의 경우에서
            # 교차하는 줄의 번호를 meets에 추가 현재줄 인덱스에 추가
            if curr_line[0] > line[0] and curr_line[1] < line[1]:
                meets[curr_idx].append(idx)
            elif curr_line[0] < line[0] and curr_line[1] > line[1]:
                meets[curr_idx].append(idx)

    return meets

meets = cross(N)
# meets.sort(key=len, reverse=True)
# print(meets)

# 가장 많이 만나는 줄부터 순차적으로 제거
def eliminate(meets:list, cnt=0):
    # 종료조건
    # meets가 차있으면 실행, 비어있으면 종료후 cnt 반환
    for meet in meets:
        if meet:
            break
    else:
        return cnt

    cables = meets
    max_meet_cable = max(enumerate(cables), key=lambda item: len(item[1]))[0]    # 길이가 max인 요소의 인덱스//gpt야 고마워!

    # 현재 줄을 다 제거해줌
    for cable in cables:
        if max_meet_cable in cable:
            cable.remove(max_meet_cable)

    cables[max_meet_cable] = [] # 마지막으로 현재줄을 없애줌
    return eliminate(cables, cnt+1)
print(eliminate(meets))