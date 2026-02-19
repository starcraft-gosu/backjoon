'''
N이 꼴랑 40개?
1. 반갈죽
2. 각 반띵마다 부분수열
3.
'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

h = N//2
arr_l = arr[:h]
arr_r = arr[h:]

