'''
순간이동은 "0"초, +- 이동은 1초
최대한 순간이동을 효율적으로 써야함
동생위치가 수빈이 앞이면 순간이동X
DFS로 해볼까..?

일단 찾아가는거먼저 구현해보자
K//2를 N보다 작아질때까지 쥰내하자
나머지가 1일때만 +1하고
작아질때 멈춘다음 어느쪽으로가는게 더 나은지만 판별하면 됨
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())


def seek(N, K):
    time = 0
    # K가 작아지기 N보다 전에 멈춤
    while K//2 > N:
        if K % 2:
            time += 1
            print(K, 1)
        K //= 2

    # 현재 K랑 K//2 중 어떤게 더 N과 가까운지 비교
    cur_r = abs(K - N)
    nex_r = abs(K//2 - N)
    print(K)
    if cur_r <= nex_r:
        time += cur_r
    else:
        time += nex_r
        if K % 2:
            time += 1
    return time

print(seek(N, K))