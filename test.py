# 백트래킹 예제: N-Queen 문제
N = 4
board = [-1] * N  # 각 행에 퀸이 있는 열 위치 저장

def is_safe(row, col):
    # 같은 열이나 대각선에 다른 퀸이 있는지 확인
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True


def backtrack(row):
    if row == N:
        print(board)  # 하나의 해답 출력
        return
    for col in range(N):
        if is_safe(row, col):
            board[row] = col       # 퀸 배치
            backtrack(row + 1)     # 다음 행으로
            board[row] = -1        # 백트래킹 (되돌리기)

backtrack(0)
