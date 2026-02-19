import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
buses = [[] for _ in range(n+1)]

for _ in range(m):
    bus = tuple(map(int, input().split()))
    a = bus[0]
    buses[a].append(bus)
print(buses)

visited = [0 for _ in range(n + 1)]
answer = [[] for _ in range(n+1)]

def dfs(x, buses, cost):
    visited[x] = 1
    stack = buses[x]
    print(stack)
    while stack:
        s, e, c = stack.pop()
        print(s, e, c)
        answer[x][e] = c
        if visited[e] == 0:
            dfs(e, buses, cost+c)

    visited[x] = 0



def search(n):
    for i in range(n):
        dfs(i+1, buses, 0)

search(n)
print(answer)

'''
모든 경로의 최소값을 출력해야한다;
경로라는건
1. 간선시작은 출발지로부터
2. 간선이 가는 모든 경로를 샅샅이 찾아보고
    pop해서 꺼내
    도착지를 보고 값을 갱신
    도착지를 출발지로 하는 놈들을 다시 넣어
3. 코스트를 유지해가며 도착지를 찾아본다음
4. 코스트를 출력. 안되면 0
5. loop가 돌수도 잇으니 visited 체크도 해줘야함
    근데 같은 곳 갓엇다고 안가면 안돼
    그럼 visited를 버스로 해야겟네
'''