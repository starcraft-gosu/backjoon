N, M = map(int, input().split())

trees = list(map(int, input().split()))
max_tree = max(trees)
trees = list(map(lambda x: max_tree - x, trees))

'''
max 길이부터 이분 탐색 진행
시간복잡도
'''

def cutting(left, right, want): # 나무 길이 조절 함수
    if right - left <= 1:
        return right


    total = 0
    cut = (left+right) // 2
    for tree in trees:
        if cut > tree:
            total += cut - tree

    # 벌목량이 목표치 M보다 작을때
    if total < want:
        left = cut
        return cutting(left, right, want)
    # 벌목량이 목표치 M보다 클때
    #
    elif total > want:
        right = cut
        return cutting(left, right, want)

    # 길이가 딱 맞을때
    else:
        return cut

first_cut = M // N
height = max_tree - cutting(0, max_tree, M)
print(height)