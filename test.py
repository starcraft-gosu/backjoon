graph = [[], [2, 3], [1], [1], [5, 6], [4], [4, 5]]  # 1-2-3 그룹, 4-5-6 그룹
visited = [False] * 7
all_groups = []  # 전체 그룹을 담을 리스트


def dfs(v, current_group):
    visited[v] = True
    current_group.append(v)  # 현재 그룹 리스트에 노드 추가
    print(current_group)

    for i in graph[v]:
        if not visited[i]:
            print(i)
            dfs(i, current_group)


# 모든 노드를 순회하며 방문하지 않은 노드 발견 시 새 그룹 시작
for i in range(1, 7):
    if not visited[i]:  # 바로 current_group에 append해줄거라 미리 visited 검증
        print("main", i)
        new_group = []
        dfs(i, new_group)  # 재귀를 돌며 new_group에 값을 채움
        all_groups.append(new_group)

print(all_groups)  # 출력: [[1, 2, 3], [4, 5, 6]]