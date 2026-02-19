# import sys
# input = sys.stdin.readline
# from collections import defaultdict
#
# # x 노드 삭제
# def del_child(tree, x):
#     n_p = tree.pop(x, None) # default없으면 keyError
#     # x의 자식 노드 삭제
#     if n_p:
#         for p in n_p:
#             del_child(tree, p)
#     # x 노드 삭제
#     for node in tree:
#         if tree[node] == [x]:
#             tree.pop(node)
#             break
#         elif x in tree[node]:
#             tree[node].remove(x)
#             break
#     return tree
#
#
# n = int(input())
# parents = list(map(int, input().split()))
# x = int(input())
#
# # value로 자식 노드를 갖는 트리 dict로 구현
# tree = defaultdict(list)
# for i in range(n):
#     tree[parents[i]].append(i)
# # tree = {-1: [0], 0: [1, 2], 1: [3, 4]}
#
# answer = 0
# if x in tree[-1]:
#     print(answer)
# else:
#     new_tree = del_child(tree, x) # 노드 삭제 후 트리
#     # print(new_tree, 1, new_tree.values())
#     # 만들어진 트리의 리프 노드 개수 세기
#     # print(new_tree)
#     for nodes in new_tree.values():
#         for node in nodes:
#             if node not in new_tree:
#                 answer += 1
#     print(answer) # x를 빼줘야함

#-----------------------------------------------------------------------------
N = int(input())
parentdata = list(map(int, input().split()))
erasenode = int(input())


def dfs_delete(node):
    parentdata[node] = -2  # 제거함
    for i in range(N):
        if node == parentdata[i]:  # 재귀를 통해 삭제
            dfs_delete(i)


dfs_delete(erasenode)
print(parentdata)
counter = 0
for i in range(N):
    if parentdata[i] != -2 and i not in parentdata:  # 제거되지 않고 남아있는 노드 i의 자식이 없다면
        counter += 1

print(counter)