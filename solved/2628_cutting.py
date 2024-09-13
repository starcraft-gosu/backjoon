# for 문 돌려서 입출력 값 받는 함수 생성
# cnt
# 그걸 for문으로 돌려

def bubble_sort(arr):                               # input 오름차순 정렬
    for i in range(len(arr)):
        for j in range(len(arr)-i-2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def square(g1, g2, c1, c2):                         # 가로 세로 정보로 넓이 구하기
    cnt = 0
    for _ in range(g1, g2):
        for _ in range(c1, c2):
            cnt += 1
    lst_cnt.append(cnt)                             # 넓이 정보를 리스트에 추가

N, M = map(int, input().split())
K = int(input())

garo = [0]                                          # 최초 구간 0 ~ a를 위해 0 추가
cero = [0]
for _ in range(K):
    a, b = map(int, input().split())
    if a == 0:
        cero.append(b)
    else:
        garo.append(b)
garo.append(N)                                      # [0, 4, 10]    마지막 구간 위해 추가
cero.append(M)                                      # [0, 3, 2, 10] 마지막 구간 위해 추가
bubble_sort(garo)                                   # [0, 4, 10]
bubble_sort(cero)                                   # [0, 2, 3, 8]

lst_cnt = []                                        # 사각형 크기정보 넣는 리스트
for i in range(len(garo)-1):                        # 인덱스로 가로 세로 리스트에 접근해
    for j in range(len(cero)-1):
        square(garo[i], garo[i+1], cero[j], cero[j+1])  # 사각형 넓이 함수에 인자 추가

max = 0
for x in lst_cnt:
    if max < x:
        max = x
print(max)